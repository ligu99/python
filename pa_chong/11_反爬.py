"""
代理
"""
import requests
import random

ips = ['221.222.84.131:9000', '124.42.7.103:80']
ips2 = ['http://211.142.96.250:9091', 'http://223.94.85.131:9091', 'http://39.130.150.44:80']    # IP前面是否要协议，看情况而定
proxy = {
    # 'http': random.choice(ips)
    'https': "https://218.68.8.83:3129"    # http 或者 https 看请求的网站而定
}
url = "https://www.baidu.com"
res = requests.get(url, proxies=proxy)
res.encoding = "utf-8"
print(res.text)
