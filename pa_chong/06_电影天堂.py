# coding=gbk
import requests
import re

domain = "https://www.dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/103.0.0.0 Safari/537.36"
}

page_content = requests.get(domain, headers=headers, verify=False)     # verify=False 去掉安全验证

page_content.encoding = "gbk"

# print(page_content.text)

pattern = re.compile(r'2022必看热片.*?<ul>(?P<movie>.*?)</ul>', re.S)
pattern2 = re.compile(r"<li><a href='(?P<href>.*?)'.*?", re.S)
pattern3 = re.compile(r'<h1>(?P<name>.*?)</h1>.*?<td style="WORD-WRAP: break-word".*?<a href="(?P<downaddr>.*?)"', re.S)


res = pattern.finditer(page_content.text)

subHrefList = []
for item in res:
    # print(item.group("movie"))
    movies = item.group("movie")
    res2 = pattern2.finditer(movies)
    # 获取子页面链接
    for it in res2:
        # print(it.group("href"))
        subHrefList.append(domain + it.group("href").strip("/"))

# print(subHrefList)

stream = open('ddyt2022_bikan.txt', mode='w', encoding='utf-8')
for index, h in enumerate(subHrefList):     # enumerate 解决too many values to unpack (expected 2)
    index += 1
    sp_content = requests.get(h, headers=headers, verify=False)
    sp_content.encoding = "gbk"
    res3 = pattern3.search(sp_content.text)
    # print(res3.group("name"), res3.group("downaddr"))
    stream.write(f'{index}.{res3.group("name")}\n   下载地址：{res3.group("downaddr")}\n')
