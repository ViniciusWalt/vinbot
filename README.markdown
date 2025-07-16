# VINBOT 🤖

## Descrição 🤖
VINBOT é um script Python que envia mensagens automáticas para o WhatsApp usando a API da WHAPI. O projeto foi desenvolvido para enviar uma mensagem personalizada, como "Olá, Vinicius! Bot seguro e funcionando 🚀", para um número específico.

## Pré-requisitos 🤖
- Python 3.6.0 ou superior
- Bibliotecas:
  - `requests`
  - `python-dotenv`

## Instalação 🤖

1. **Clone o repositório** (se aplicável):
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd VINBOT
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o token**:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione o token da API da WHAPI no formato:
     ```
     WHAPI_TOKEN=your_whapi_token_here
     ```

## Uso 🤖
1. Ative o ambiente virtual (conforme acima).
2. Execute o script:
   ```bash
   python send_message.py
   ```
   Isso enviará a mensagem configurada para o número `5511940289184@s.whatsapp.net`.

## Estrutura do Projeto 🤖
```
VINBOT/
├── send_message.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── venv/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    ├── pip-selfcheck.json
    └── pyvenv.cfg
```

## Configuração 🤖
- O token da API deve ser obtido da WHAPI e configurado no arquivo `.env`.
- A mensagem e o número de destino podem ser ajustados no código em `send_message.py`.

## Licença 🤖
Criado por [Vinicius Walter](https://github.com/ViniciusWalt), com ❤️ por aprendizado e automação.
