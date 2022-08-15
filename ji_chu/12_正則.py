"""
需要引入内置模块re
compile():将正则表达式模式编译成正则表达式对象，其 match() 和 search() 方法可用于匹配
原型：re.compile(pattern, flags=0)
参数：pattern 模式
     flags 模式修正符
"""
import re
re_telephon = re.compile(r"^1(([3578]\d)|(47))\d{8}$") #编译，返回正则对象

print(re_telephon.match("13600000000"))

prog = re.compile('\d{2}') # 正则对象
prog.search('100abc')  # 正则对象调用search获取匹配

"""
re.match() ：从字符串起始位置匹配一个模式，如果从起始位置匹配没有匹配成功，则返回None
原型：re.compile(pattern, flags=0)
参数：pattern 模式
     flags 模式修正符
返回值： 匹配成功返回一个Match object，失败返回None
"""
print(re.match(r'www','www.baidu.com'))

"""
re.search() : 顺序扫描字符串，找到第一个匹配项则结束
原型：re.search(pattern, string, flags=0)
参数：patter 模式
     string  要匹配的字符串
     flag  模式修正符
返回值：匹配成功，返回match object，否则返回None
"""
print(re.search(r'll','hello'))

"""
re.group()和re.groups()
re.findall() : 扫描整个字符串，并返回结果列表
re.split() ：用模式做分隔符，将字符串分隔，返回分隔列表，如果模式加上括号，则分隔符会被保留
re.sub和re.subn() ：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。
可以指定替换的次数, 如果 不指定，替换所有的匹配字符串
"""