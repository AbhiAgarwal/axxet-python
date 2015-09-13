import requests, json

requests.packages.urllib3.disable_warnings()

BASE_URL = 'https://api.axxet.io/'

def get_token(data):
    headers = {
        'content-type': 'application/json',
    }
    url = BASE_URL + 'api-key/get/'
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    json_response = json.loads(response.text)
    token = json_response['token']
    return token

token = get_token({"username": "axxet", "password": "123123"})
headers = {
    'content-type': 'application/json', 
    'Authorization': 'Bearer ' + token,
}

def axxet_get(url):
  response = requests.get(url, headers=headers, verify=False)
  json_response = json.loads(response.text)
  return json_response

def axxet_post(url, data):
  response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
  json_response = json.loads(response.text)
  return json_response

def axxet_options(url):
  response = requests.options(url, headers=headers, verify=False)
  json_response = json.loads(response.text)
  return json_response

# print axxet_get(BASE_URL + 'api/assets/')
# print axxet_options(BASE_URL + 'api/assets/')
# print axxet_get(BASE_URL + 'api/users/me/')

###### Adding new Asset
# axxet_data = {'name': 'fish'}
# print axxet_post(BASE_URL + 'api/assets/', axxet_data)
