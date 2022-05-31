# client.py
import requests
API_URL = 'http://127.0.0.1:8000'
url = '{}{}'.format(API_URL, '/quotes?tag=love')
response = requests.get(
    url, 
    headers = { }, 
    params = {'key': 'TyA0BhKO5SgCmodHzGyFlv1PqI4BqOzk0tu1gMr0Gsc'}
)
if response.status_code == 200:
    for quote in response.json():
        print(quote)
    print(len(response.json()), 'quotes returned!')
else:
    raise Exception("Invalid Request! Check your API's documentation!\n" + response.text)        
