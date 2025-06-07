# Leitor de RG com OCR

Este projeto implementa um sistema de leitura de documentos de identidade (RG) utilizando OCR (Reconhecimento Óptico de Caracteres) e validação de dados. O sistema é capaz de processar imagens de RG e extrair informações como CPF e data de nascimento.

## Funcionalidades

- Leitura de imagens de RG usando OCR
- Extração de CPF e data de nascimento
- Validação de dados extraídos
- Processamento paralelo com múltiplas threads
- Geração de gráficos de desempenho

## Requisitos

- Python 3.8+
- Bibliotecas Python (instaladas via pip):
  - pytesseract
  - opencv-python
  - numpy
  - matplotlib
  - Pillow

## Instalação

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale o Tesseract OCR:

- Windows: Baixe e instale do [site oficial](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux: `sudo apt-get install tesseract-ocr`
- macOS: `brew install tesseract`

## Uso

1. Coloque as imagens dos RGs na pasta `imagens/`

2. Execute o script principal:

```bash
python document_validator.py [número_de_threads]
```

3. Para gerar o gráfico de desempenho:

```bash
python plot_results.py
```

## Estrutura do Projeto

- `document_validator.py`: Script principal para processamento dos RGs
- `plot_results.py`: Script para geração de gráficos de desempenho
- `imagens/`: Diretório para armazenar as imagens dos RGs
- `requirements.txt`: Lista de dependências do projeto

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
