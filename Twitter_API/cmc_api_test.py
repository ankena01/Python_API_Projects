import requests , jsonpath
import secrets
from pprint import pprint as pp
from requests import Session

class CMC:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token,}
        self.session = Session()
        self.session.headers.update(self.headers)

    # GEt info for all coins
    def get_allcoins(self):
        response = self.session.get(self.apiurl + '/v1/cryptocurrency/map')
        for i in range(5):
            print(response.json()['data'][i]['name'])
        
    def get_price(self, symbol):
        response = self.session.get(self.apiurl + '/v1/cryptocurrency/quotes/latest' , params={'symbol' : symbol})
        #print(response.status_code)
        return response.json()
    


cmc  = CMC(secrets.API_KEY)
#cmc.get_allcoins()
#pp(cmc.get_price('BTC,ETH'))
pp(cmc.get_price('BTC')['data']['BTC']['quote']['USD']['price'])