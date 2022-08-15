# coding=gbk
import requests
from bs4 import BeautifulSoup
import time

domain = "https://www.dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/103.0.0.0 Safari/537.36"
}

page_content = requests.get(domain, headers=headers, verify=False)
page_content.encoding = "gbk"
res = BeautifulSoup(page_content.text, "html.parser")   # html.parser 声明传入的BeautifulSoup的内容是html

"""
bs方法：
1.find(标签,属性=值)
2.find_all(标签，属性=值)
"""
divList = res.find("div", class_="co_content222")     # class是py的关键字
divList2 = divList.find_all("li")[1:]
# print(divList2)
for item in divList2:
    item_a = item.find("a")
    # print(item_a["href"])
    sub_page_content = requests.get(domain+item_a["href"].strip("/"))
    sub_page_content.encoding = "gbk"
    sub_page_res = BeautifulSoup(sub_page_content.text, "html.parser")
    img = sub_page_res.find("div", id="Zoom")
    img_src = img.find("img")["src"]
    # print(img_src)
    img_name = img_src.split("/")[-1]
    img_res = requests.get(img_src)
    with open(f"img/{img_name}", mode="wb") as img:
        img.write(img_res.content)
    time.sleep(0.5)
print("OK")
