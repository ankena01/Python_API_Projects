import requests , jsonpath
import secrets
from pprint import pprint as pp

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

response = requests.get(url , headers=headers)

print(response.status_code)

#print(response.json())

pp(response.json())
