"""
定義：
def 函数名(参数列表): //实现特定功能的多行代码 [return [返回值]]
注意：
def关键字、函数名()和冒号是固定写法
函数名则是根据函数的功能来命名，一般要求做到见名知意
参数列表根据情况可以有一个、两个、多个，如果有两个或者以上，使用逗号隔开
函数体就是实现函数功能的代码段，函数体属于函数中的内容，前面需要一个缩进
[return [返回值]]表示可选，即返回值的内容可以有也可以没有取决于开发需求

調用：
[返回值 =] 函数名([实参列表])
"""

from ast import arg
import random
# n默認值為4
def vd_code(n=4):
    s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456"
    code = ""
    for i in range(n):
        r = random.choice(s)
        code += r
    return code

c = vd_code()
print(c)
d = vd_code(5)
print(d)

"""
可变参数
使用：*args或者**kwargs
"""

def add(*args):  # args即arguments的简写   *args 在函数中使用的时候就是一个()
    print(type(args)) # 是个元组类型

    if len(args)>1:
        sum = 0
        for i in args:
            sum += i
            
        print("和：",sum)
    else:
        print("至少兩個參數")

add()
add(1)
add(1,2)

def func(**kwargs):   # kwargs 即  key word  arguments  ，而**kwargs 就是一个字典类型的
 print(kwargs)   # 即字典保存关键字参数 {'a':1,'b':2,'c':3}
 
func(a=1,b=2,c=3)

def no_res():
    print("1")

res1 = no_res()
print("返回結果：{}".format(res1)) #None 因为没有return关键字

def has_res():
    return 10
res2 = has_res()
print("返回結果：{}".format(res2)) #返回結果：10



def res_more():
  return 'hello',666
  
# 调用函数并获取返回值
res3 = res_more()
print(res3) # ('hello',666) 如果return后面有多个返回值则将多个返回值保存在元组中，最后以元组的形式整体返回