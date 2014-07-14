import requests
import json

API_KEY = 'key'

uri = raw_input("Enter your url to shorten: ")

params = {'access_token':API_KEY, 'uri':uri}

endpoint = 'https://api-ssl.bitly.com/v3/shorten'

r = requests.get(endpoint, params=params)

response = json.loads(r.text.decode('utf-8'))

print response['data']['url']
