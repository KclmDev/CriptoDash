# Monitoramento de Criptomoedas

Este projeto é um dashboard interativo que permite visualizar o histórico de preços de diversas criptomoedas. Desenvolvi essa aplicação para mostrar boas praticas na integração de APIs públicas, além de criar uma interface amigável para visualização de dados financeiros.

## Sobre o Desenvolvimento

Ao construir este projeto, apliquei conceitos de Clean Architecture separando o código em três camadas:

1. Service: Isolamento da lógica de requisição HTTP (Requests).
2. Business: Tratamento de dados brutos e conversão de timestamps (Pandas).
3. UI: Exibição dos dados e gráficos (Streamlit).

## Tecnologias

* Python: Linguagem de programação
* Streamlit: Para construção da interface web
* Pandas: Manipulação de dados e dataframes

## Como rodar localmente

Clone o projeto:
git clone 

crie seu ambiente virtual (venv):
windows:
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
mac: 
    python3 -m venv .venv
    source .venv/bin/activate

instale as dependências (dentro do venv):
pip install -r requirements.txt

Crie um arquivo .env na raiz com a seguinte variável:
BASE_URL=https://api.coingecko.com/api/v3

Para rodar a aplicação:
streamlit run app.py
