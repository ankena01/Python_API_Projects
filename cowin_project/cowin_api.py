import requests
from pprint import pprint as pp

PINCODE = '411036'
REQ_DATE = "24-11-2021"
header = {'User-Agent':'Chrome/84.0.4147.105 Safari/537.36'}
url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}'

response = requests.get(url , headers=header)

total_centers = len(response.json()['centers'])
print(total_centers)

