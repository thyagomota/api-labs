# client.py
import requests
API_URL = 'http://127.0.0.1:8000'
url = '{}{}'.format(API_URL, '/quotes/0')
response = requests.get(
    url, 
    headers = { }, 
    params = { }
)
if response.status_code == 200:
    print(response.json())
else:
    raise Exception("Invalid Request! Check your API's documentation!\n" + response.text)        
