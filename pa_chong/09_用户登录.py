import requests
import json

url = "http://azdockerq.mtel.ws:5215/api/cms/admin/login"
data = {
    "account":  "admin",
    "password": "123456"
}
string = json.dumps(data)
headers = {
    "Content-Type": "application/json"
}

session = requests.session()
resp = requests.post(url, data=string, headers=headers)
print(resp.text)
