import requests 
import pprint
import json
import random
# url即百度首页的链接
url = 'https://www.baidu.com' 
# 通过get方法向目标url发送get请求，返回响应的结果，是一个response对象
response = requests.get(url)
# 打印响应内容
print(response)

"""
response.text 读取服务器响应的内容,通常使用response.text会自动解码来自服务器的内容。因此大多数 unicode 字符集都能被无缝地解码

response.encoding 获取文本编码，也可以使用该属性修改编码

response.content 获取响应内容的二进制形式，一般图片、音视频等使用此方式获取

response.status_code 获取当前请求的响应码

response.headers 获取响应的响应头

response.cookies 获取响应的cookies内容

response.url 获取请求的url
"""

"""
使用requests保存图片，则需要结合文件保存完成
"""
# 图片地址
image_url = 'https://anchorpost.msstatic.com/cdnimage/anchorpost/1082/bc/\
e60d649dd5fa645b575f73f9aef0bc_2168_1617694516.jpg?imageview/4/0/w/338/h/19'
# 发送请求获取响应
response = requests.get(url)

with open('../img/girl.png', 'wb')as f:
    f.write(response.content)

# 检索阿凡达的信息
url = 'https://www.douban.com/search?q=%E9%98%BF%E5%87%A1%E8%BE%BE'
# 定义headers请求头
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
  Chrome/80.0.3987.162 Safari/537.36"
}
# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
# 使用pprint进行格式化的输出
# pprint.pprint(response.text)

response.close()    # 关闭请求


"""
带参数的两种请求方式
1.直接跟在请求链接的后面，如https://www.baidu.com/s?wd=python。wd=python就是参数。多个参数之间使用符号【&】链接
2.使用params实现，类似headers的使用。先定义一个字典params ={'wd':'Python','pn':10}
"""

# requests.get(url, headers=headers,params=params)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/80.0.3987.162 Safari/537.36"}
# 下面的url如果使用params可以省略?
url = 'https://www.baidu.com/s' 
# 请求参数是一个字典 即wd=Python和pn=10
params = {'wd': 'Python', 'pn': 10}
# 在params上设置字典
response = requests.get(url, headers=headers, params=params) 
# 获取结果并打印
# print(response.text)


"""
post请求
response = requests.post("请求地址", data = 字典类型的参数,headers=字典类型的请求头)
"""
data = {
    'a': '好好学习，天天向上！',
    'b': '强身健体，天天Happy'
}
# 发送网络请求
response = requests.post('http://httpbin.org/post', data=data)
print(type(response.json()), response.json())   # 打印转换后的响应数据


"""
IP代理
http://ip.kxdaili.com/ 开心代理
https://proxy.mimvp.com/free.php 米扑代理
http://www.xiladaili.com/ 西拉免费代理IP
http://ip.jiangxianli.com/ 免费代理IP库
http://www.superfastip.com/ 极速代理
https://proxy.mimvp.com/free.php 米扑代理
http://www.shenjidaili.com/open/ 神鸡代理IP
http://31f.cn/http-proxy/ 三一代理
http://www.feiyiproxy.com/?page_id=1457 飞蚁代理
http://ip.zdaye.com/dayProxy/2019/4/1.html 站大爷
http://www.66ip.cn 66免费代理网
https://www.kuaidaili.com/free/inha 快代理
https://www.xicidaili.com 西刺
http://www.ip3366.net/free/?stype=1 云代理
http://www.iphai.com/free/ng IP海
http://www.goubanjia.com/ 全网代理
http://www.89ip.cn/index.html 89免费代理
http://www.qydaili.com/free/?action=china&page=3 旗云代理
"""
#  代理的使用
url = "https://www.baidu.com"
# 获取的代理ip地址，放在一个字典中，可以写多个使用随机数不断变化选取
# 注意：免费代理的地址是有失效时间的，自己可以去上面网站找合适的
ips = ['221.222.84.131:9000', '124.42.7.103:80', '116.214.32.51:8080', '222.73.68.144:8090', '117.121.100.9:3128']
proxy = {
    'http': random.choice(ips),
}

response = requests.get(url, proxies=proxy)

print(response.text)
