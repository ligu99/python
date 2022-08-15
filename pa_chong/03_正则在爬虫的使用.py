"""
re模块的常用方法
使用 re模块下的compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象。
通过 Pattern 提供的一系列方法可以对文本进行匹配查找，最后得到一个Match对象
最后使用 Match 对象提供的属性和方法获得信息
"""
import requests

import re
# 将正则表达式编译成 Pattern 对象
pattern = re.compile(r'\w{3}')
print(pattern)
"""
Pattern 对象的一些常用方法主要有：

match 方法：从起始位置开始查找，一次匹配
search 方法：从任何位置开始查找，一次匹配
findall 方法：全部匹配，返回列表
finditer 方法：全部匹配，返回迭代器
split 方法：分割字符串，返回列表
sub 方法：替换
"""
# 1. 得到pattern
pattern = re.compile('abc')
# 2. 使用公式对象匹配要校验的字符串  match 匹配，返回一个匹配对象match对象
match_obj = pattern.match('helloabc')
print(match_obj)    # None Match在匹配判断的时候都是从字符串的开头开始判断，如果开始没有匹配上就返回None

r = re.search('abc', 'helabcloabc')
print(r)    # Match 对象

"""
group(): 用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)

span(): 返回匹配字符串的起始位置

start()：用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；

end()：用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0
"""
if r:
    print(r.group())
    print(r.span())
    print(r.start())
    print(r.end())


url = "http://www.baidu.com/"
response = requests.get(url)
response.encoding = 'utf-8'
content = response.text
# 此处使用findall结合正则表达式完成
title = re.findall(r'<title>(.*?)</title>', content)
print(title[0])

# 定义正则表达式获取所有网页的超链接
res = r"<a.*?href=.*?<\/a>"
urls = re.findall(res, content)
for u in urls:
    print(u)

# 获取超链接中的内容
res2 = r'<a .*?>(.*?)</a>'
texts = re.findall(res2, content, re.S | re.M)
for t in texts:
    print(t)

# 抓取标签中的参数
all_urls = '\n'.join(urls)
# 定义正则表达式
res3 = r"(?<=href=)http:.+?(?=\>)|(?<=href=)http:.+?(?=\s)"
# 查找符合规则的超级链接
urls2 = re.findall(res3, content, re.I|re.S|re.M)
for url in urls2:
    print(url) 

