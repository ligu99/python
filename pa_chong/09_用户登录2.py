import requests
import json

url = "http://azdockerq.mtel.ws:5215/api/cms/admin/login"
url2 = "..."


data = {
    "account":  "admin",
    "password": "123456"
}
string = json.dumps(data)
headers = {
    "Content-Type": "application/json"
}

session = requests.session()
resp = session.post(url, data=string, headers=headers)
print(resp.text)
print(resp.cookies)     # set-cookies
 
# 登录后获取其他页面的数据
resp2 = session.get(url2)
print(resp2.json())


# 方式二 直接在headers添加cookies
"""
headers = {
    "Cookies": "..."
}
"""