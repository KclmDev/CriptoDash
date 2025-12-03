import streamlit as st
from src.services.api_service import CoinGeckoClient
from src.business.analytics import process_crypto_data

@st.cache_data
def load_data(coin_id, days):
    client = CoinGeckoClient()
    raw_data = client.get_coin_history(coin_id, days)
    df = process_crypto_data(raw_data)
    return df

def render_dashboard():
    st.title("Monitoramento de Criptomoedas")
    st.markdown("---")

    st.sidebar.header("Configurações")

    crypto_list = ['bitcoin', 'ethereum','dogecoin','ripple', 'litecoin', 'cardano', 'polkadot', 'stellar', 'chainlink']
    coin = st.sidebar.selectbox("Selecione a moeda:", crypto_list)

    days = st.sidebar.slider("Período (dias):", min_value=7, max_value=365, value=30)

    data_load_state = st.text("Carregando dados...")
    df = load_data(coin, days)
    data_load_state.empty()
    
    if df is not None:
        st.subheader(f"Histórico de Preço de {coin.title()}")
        st.line_chart(df, x='data', y='preço')
        
        current_price = df['preço'].iloc[-1]
        start_price = df['preço'].iloc[0]
        price_change_pct = ((current_price - start_price) / start_price) * 100
        st.metric(
            label=f"Preço Atual ({days}d)",
            value=f"US$ {current_price:,.2f}",
            delta=f"{price_change_pct:.2f}%"
        )
        with st.expander("Ver Tabela de dados brutos"):
            st.dataframe(df)
    
    else:
        st.error(f"Não foi possível carregar os dados históricos de {coin.title()}. Tente novamente ou verifique sua conexão.")