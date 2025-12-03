primeiro passo = instalar venv e ativar
    windows:
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    
    mac: 
    python3 -m venv .venv
    source .venv/bin/activate

segundo passo = com venv ativo instalar as bibliotecas
pip install -r requirements.txt

terceiro passo = com tudo instalado rodar a aplicação
streamlit run app.py