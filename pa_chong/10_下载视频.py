"""
防盗链
headers = {
    "Refere":"。。。"
}
"""
import requests

url = "..."

# URL 替换 将aaa替换为bbb
# url2 = url.replace("aaa", "bbb")

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(url).content)
