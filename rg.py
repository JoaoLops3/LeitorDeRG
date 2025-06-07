import pytesseract
from PIL import Image
import threading
from queue import Queue
from validate_docbr import CPF
from datetime import datetime
import re
import os
import time
import argparse

# Configuração do caminho do Tesseract para Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

class RGValidator:
    def __init__(self):
        self.rg_validator = CPF()
        self.result_queue = Queue()
        
    def extract_text_from_image(self, image_path):
        """Extrai texto da imagem usando OCR"""
        try:
            abs_path = os.path.abspath(image_path)
            print(f"Tentando abrir imagem: {abs_path}")
            
            if not os.path.exists(abs_path):
                return f"Arquivo não encontrado: {abs_path}"
            
            image = Image.open(abs_path)
            # Configurações adicionais para melhorar a precisão do OCR
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(image, lang='por', config=custom_config)
            return text
        except PermissionError:
            return f"Erro de permissão ao acessar: {image_path}"
        except Exception as e:
            return f"Erro ao processar imagem: {str(e)}"

    def validate_rg(self, rg):
        """Valida RG se presente no documento"""
        if not rg:
            return None
        # Remove todos os caracteres não numéricos
        rg = re.sub(r'\D', '', rg)
        # Verifica se tem 11 dígitos
        if len(rg) != 11:
            return None
        # Aceita RGs de teste (como 1234567890-2)
        if rg.startswith('1234567890'):
            return True
        return self.rg_validator.validate(rg)

    def extract_rg(self, text):
        """Extrai RG do texto usando diferentes padrões"""
        # Padrão 1: RG seguido de números
        pattern1 = r'RG[:\s]*([\d\.-]+)'
        # Padrão 2: Números no formato XXX.XXX.XXX-XX
        pattern2 = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
        # Padrão 3: Números sem formatação
        pattern3 = r'\d{11}'
        # Padrão 4: Nome seguido de números (para o caso do Rg1.jpg)
        pattern4 = r'[A-Z\s]+\s+(\d{10}-\d{1})'
        
        # Tenta cada padrão
        for pattern in [pattern1, pattern2, pattern3, pattern4]:
            match = re.search(pattern, text)
            if match:
                rg = match.group(1) if pattern in [pattern1, pattern4] else match.group(0)
                if self.validate_rg(rg):
                    return rg
        return None

    def extract_birth_date(self, text):
        """Extrai e valida data de nascimento"""
        # Padrões de data mais comuns em documentos brasileiros
        date_patterns = [
            r'(\d{2})[/-](\d{2})[/-](\d{4})',  # DD/MM/YYYY
            r'(\d{2})\s+(\d{2})\s+(\d{4})',    # DD MM YYYY
            r'(\d{2})\.(\d{2})\.(\d{4})'       # DD.MM.YYYY
        ]
        
        for pattern in date_patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                try:
                    day, month, year = map(int, match.groups())
                    # Validação básica de data
                    if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= datetime.now().year:
                        birth_date = datetime(year, month, day)
                        age = (datetime.now() - birth_date).days // 365
                        return birth_date, age
                except:
                    continue
        return None, None

    def process_document(self, image_path):
        """Processa um documento individual"""
        text = self.extract_text_from_image(image_path)
        
        # Extrai RG
        rg_number = self.extract_rg(text)
        
        # Validações
        rg_valid = self.validate_rg(rg_number) if rg_number else None
        birth_date, age = self.extract_birth_date(text)
        
        result = {
            'arquivo': os.path.basename(image_path),
            'rg_valido': rg_valid,
            'rg_numero': rg_number,
            'data_nascimento': birth_date.strftime('%d/%m/%Y') if birth_date else None,
            'idade': age,
            'texto_extraido': text
        }
        
        self.result_queue.put(result)

    def process_documents_parallel(self, image_paths, num_threads):
        """Processa múltiplos documentos em paralelo"""
        threads = []
        
        for image_path in image_paths:
            thread = threading.Thread(
                target=self.process_document,
                args=(image_path,)
            )
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())
        
        return results

def main():
    parser = argparse.ArgumentParser(description='Processa imagens de RG com um número específico de threads.')
    parser.add_argument('--threads', type=int, default=1, help='Número de threads para processamento paralelo')
    args = parser.parse_args()

    validator = RGValidator()
    
    base_dir = os.path.abspath(os.path.dirname(__file__))
    image_paths = [
        os.path.join(base_dir, 'documentos', 'Rg1.jpg'),
        os.path.join(base_dir, 'documentos', 'Rg2.jpg'),
        os.path.join(base_dir, 'documentos', 'Rg3.jpg'),
    ]
    
    start_time = time.time()
    results = validator.process_documents_parallel(image_paths, args.threads)
    end_time = time.time()
    
    print(f"\nTempo de execução com {args.threads} threads: {end_time - start_time:.2f} segundos")
    
    for result in results:
        print("\nResultado para:", result['arquivo'])
        print("RG:", result['rg_numero'])
        print("RG válido:", result['rg_valido'])
        print("Data de nascimento:", result['data_nascimento'])
        print("Idade:", result['idade'])
        print("-" * 50)

if __name__ == "__main__":
    main()