import requests
import json
import apikey

url = "https://www.alphavantage.co/query"

data = {
	'function': 'TIME_SERIES_INTRADAY',
	'symbol': '^GSPC',
	'interval': '1min',
	'apikey': apikey.API_KEY,
}

response = requests.get(url, params=data)

print response.url
print response.content
