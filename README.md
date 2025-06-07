# Leitor de RG

Este projeto realiza a leitura automática de imagens de RG (Registro Geral) utilizando OCR (Reconhecimento Óptico de Caracteres) e validação de dados extraídos, como número do RG e data de nascimento.

## Como usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/JoaoLops3/LeitorDeRG.git
   cd LeitorDeRG
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Instale o Tesseract OCR:**

   - Baixe e instale o Tesseract para Windows: [Tesseract no Windows](https://github.com/UB-Mannheim/tesseract/wiki)
   - O caminho padrão utilizado no código é `C:\Program Files\Tesseract-OCR`. Se instalar em outro local, ajuste o caminho no arquivo `rg.py`.

4. **Coloque as imagens dos RGs na pasta `documentos/`**

   - Os arquivos devem ser imagens (JPG, PNG, etc.)
   - Exemplo: `documentos/Rg1.jpg`, `documentos/Rg2.jpg`, ...

5. **Execute o projeto:**
   ```bash
   python rg.py
   ```

## Saída esperada

O programa irá exibir para cada imagem:

- Nome do arquivo
- RG extraído
- Se o RG é válido
- Data de nascimento
- Idade

## Bibliotecas utilizadas

- **pytesseract**: Interface Python para o Tesseract OCR
- **Pillow**: Manipulação de imagens
- **validate-docbr**: Validação de documentos brasileiros (usado para simular validação de RG)
- **threading/queue**: Processamento paralelo das imagens
- **re**: Expressões regulares para extração de dados
- **datetime**: Cálculo de idade e validação de datas

---

Se tiver dúvidas ou sugestões, fique à vontade para abrir uma issue ou contribuir!
