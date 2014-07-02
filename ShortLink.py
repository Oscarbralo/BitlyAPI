from urllib.request import urlopen
import json

API_KEY = 'key'

endpoint = 'https://api-ssl.bitly.com/v3/shorten?access_token='
endpoint += API_KEY
endpoint += '&uri=http://'
endpoint += input("Enter your url to shorten: ")
endpoint += '&format=json'

def getResponse(endpoint):
	return str(urlopen(endpoint).read().decode('utf-8'))

def loadJsonResponse(response):
	return json.loads(response)

response = getResponse(endpoint)
result = loadJsonResponse(response)
print("Shorted url: " + result['data']['url'])