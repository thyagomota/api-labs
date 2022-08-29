# client.py
import requests
API_URL = 'http://127.0.0.1:8000'
url = '{}{}'.format(API_URL, '/quotes/4546')
response = requests.get(
    url, 
    headers = { }, 
    params = { }
)
if response.status_code == 200 or response.status_code == 404:
    print(response.status_code)
    print(response.json())
else:
    raise Exception("Invalid Request! Check your API's documentation!\n" + response.text)        
