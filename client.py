import requests, json

BASE_URL = 'https://api.axxet.io/'

headers = {'content-type': 'application/json'}
url = BASE_URL + 'api-key/get/'
data = {"username": "axxet", "password": "123123"}

response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
json_response = json.loads(response.text)
token = json_response['token']

url = BASE_URL + 'api/assets/'
headers = {'Authorization': 'JWT ' + token}
response = requests.get(url, headers=headers, verify=False)
json_response = json.loads(response.text)
print json_response

headers = {'Authorization': 'JWT ' + token}
response = requests.options(url, headers=headers, verify=False)
json_response = json.loads(response.text)
print json_response