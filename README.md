# Validador de Documentos com OCR Paralelo

Este sistema permite validar documentos (RG, CPF) usando OCR em processamento paralelo.

## Requisitos

- Python 3.7+
- Tesseract OCR instalado no sistema
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Instale o Tesseract OCR:

   - Windows: Baixe e instale de https://github.com/UB-Mannheim/tesseract/wiki
   - Linux: `sudo apt-get install tesseract-ocr`
   - Mac: `brew install tesseract`

2. Instale as dependências Python:

```bash
pip install -r requirements.txt
```

## Estrutura de Diretórios

```
.
├── document_validator.py
├── requirements.txt
└── documentos/
    ├── rg1.jpg
    ├── rg2.jpg
    └── ...
```

## Como Usar

1. Coloque as imagens dos documentos na pasta `documentos/`
2. Modifique a lista `image_paths` no arquivo `document_validator.py` para incluir os caminhos das suas imagens
3. Execute o script:

```bash
python document_validator.py
```

## Funcionalidades

- Extração de texto usando OCR
- Validação de RG
- Validação de CPF
- Extração e validação de data de nascimento
- Processamento paralelo de múltiplos documentos
- Suporte para imagens em formato JPG/PNG

## Observações

- O OCR funciona melhor com imagens claras e bem iluminadas
- O sistema assume que os documentos estão em português
- A validação de RG e CPF segue os padrões brasileiros
