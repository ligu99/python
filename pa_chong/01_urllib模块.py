"""
Content-Type
Host (主机和端口号)
Connection (链接类型)
Upgrade-Insecure-Requests (升级为HTTPS请求)
User-Agent (浏览器名称)
Referer (页面跳转处)
Cookie (Cookie)
Authorization(用于表示HTTP协议中需要认证资源的认证信息，如前边web课程中用于jwt认证)
"""

"""
urllib库
urllib.request请求模块
urllib.error 异常处理模块
urllib.parse 解析模块
urllib.robotparser 文件解析模块
"""
from urllib import request, parse,error
from urllib.parse import urlencode,quote,unquote

url = 'http://httpbin.org/post'
# 请求头设置
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
 'Host': 'httpbin.org'
}
# 参数设置
dict = {
 'name': 'Germey'
}
# 将参数转成字节形式
data = bytes(parse.urlencode(dict), encoding='utf8')
# 创建Request对象
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 使用urlopen发出请求
response = request.urlopen(req)
# 读取并打印结果
print(response.read())


# 一个不存在的网址链接
url = "http://www.nonepython.com"
req = request.Request(url)
try:
    response = request.urlopen(req)
    print('状态码：'+str(response.getcode()))
    html = response.read().decode('utf-8')
    print(html)
except error.URLError as e:
    print('错误：',e.reason)

"""
urllib.parse
对于构造GET请求参数时非常有用，首先声明一个字典将参数表示出来，然后调用urlencode的方法将其序列化为GET请求参数
"""
params = {'name':'小明','age':20}
base_url = 'http://baidu.com?'
base_url += urlencode(params)
print(base_url)

"""
quote
该方法将内容转化为URL编码格式，此方法可以将中文字符串转化为URL编码
"""
keyword = '美女'
url = 'http://www.baidu.com?wd=' +quote(keyword)
print(url) #http://www.baidu.com?wd=%E7%BE%8E%E5%A5%B3

# unquote：利用unquote进行还原
print(unquote("%E7%BE%8E%E5%A5%B3")) #美女

"""
urlretrieve(url, filename=None, reporthook=None, data=None)
1.参数 url 指定了要下载的文件的url
2.参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
3.参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，
我们可以利用这个回调函数来显示当前的下载进度。
4.参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，
filename 表示保存到本地的路径，header 表示服务器的响应头。
"""
image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fdingyue.nosdn.127.net%2FwFdkoX0pkLJoS1Ued6ou7dgUMaiZfAy93RiVXhz3iy7QU1542769981593compressflag.jpeg&refer=http%3A%2F%2Fdingyue.nosdn.127.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620297676&t=0b3443d8c5b502c8134079e0e131ef3f'
request.urlretrieve(image_url,'img/liying.jpg')