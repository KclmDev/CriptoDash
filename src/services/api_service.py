import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL', 'https://api.coingecko.com/api/v3')
if not BASE_URL:
    BASE_URL = 'https://api.coingecko.com/api/v3'
    
class CoinGeckoClient:
    def get_coin_history(self, coin_id, days):
        url = f"{BASE_URL}/coins/{coin_id}/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': 'daily'
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                return response.json()
            
            print(f"Erro na requisição (Status {response.status_code}):{response.text}")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
            return None