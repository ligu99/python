import requests

url = "https://fanyi.baidu.com/sug"
s = input("输入内容：")

dat = {
    "kw": s
}

resp = requests.post(url, data=dat)
print(resp.json()["data"])
