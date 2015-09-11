import requests, json

requests.packages.urllib3.disable_warnings()

BASE_URL = 'https://api.axxet.io/'

headers = {'content-type': 'application/json'}
url = BASE_URL + 'api-key/get/'
data = {"username": "axxet", "password": "123123"}

response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
json_response = json.loads(response.text)
token = json_response['token']
headers = {'Authorization': 'Bearer ' + token}

def axxet_get(url):
  response = requests.get(url, headers=headers, verify=False)
  json_response = json.loads(response.text)
  return json_response

def axxet_options(url):
  response = requests.options(url, headers=headers, verify=False)
  json_response = json.loads(response.text)
  return json_response

print axxet_get(BASE_URL + 'api/assets/')
# print axxet_options(BASE_URL + 'api/assets/')
# print axxet_get(BASE_URL + 'api/users/me/')