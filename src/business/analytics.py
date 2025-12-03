import pandas as pd

def process_crypto_data(raw_data):
    if raw_data is None:
        return None
    
    prices = raw_data.get('prices', [])
    market_caps = raw_data.get('market_caps', [])
    total_volumes = raw_data.get('total_volumes', [])
    
    if not prices or not market_caps or not total_volumes:
        return None
    
    df_prices = pd.DataFrame(prices, columns=['data', 'preço'])
    df_caps = pd.DataFrame(market_caps, columns=['data', 'capitalizacao']) 
    df_volumes = pd.DataFrame(total_volumes, columns=['data', 'volume'])
    df_merged = pd.merge(df_prices, df_caps, on='data', how='inner')
    df_final = pd.merge(df_merged, df_volumes, on='data', how='inner')
    df_final['data'] = pd.to_datetime(df_final['data'], unit='ms')
    
    return df_final