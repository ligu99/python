import requests
from lxml import etree
import time

url = "https://book.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/103.0.0.0 Safari/537.36"
}
# stream = open('douban_dushu.txt', mode='a', encoding='utf-8')


def wrfile(res_list):
    for item in res_list:
        index = item.xpath("./div[1]/strong/text()")[0]
        name = item.xpath("./div[2]/h2/a/text()")[0]
        print(f'{index}.{name}')
        # stream.write(f'{index}.{name}\n')


def get_page(prams):
    # print(prams)
    page_content = requests.get(url + prams, headers=headers)
    # print(page_content.text)
    html = etree.HTML(page_content.text)
    now = html.xpath("/html/body/div[3]//div[@class='xbar']/div/span[@class='now']/span/text()")[0]
    stream.write(now + "\n")
    print(now)
    rest_list = html.xpath("/html/body/div[3]//ul[@class='chart-dashed-list']/li")
    wrfile(rest_list)
    time.sleep(5)
    if prams == "?subcat=all":
        type_list = html.xpath("/html/body/div[3]//div[@class='xbar']/div/a/@href")
        for it in type_list:
            get_page(it)


get_page("?subcat=all")





