"""
内置函數：
bool() 将给定的数据类型转换成bool值.如果不给值.返回False
int () 将给定的数据转换成int值.如果不给值,返回0
float () 将给定的数据转换成float值.也就是小数
complex () 创建一个复数.第一个参数为实部，第二个参数为虚部.或者第一个参数直接用字符串来描述复数

bin() 将给的参数转换成二进制
otc() 将给定的参数转换成八进制
hex() 将给定的参数转换成十六进制

abs() 返回绝对值
divmode() 返回商的余数
round () 四舍五入
pow(a,b) 求a 的b 次幂,如果有三个参数.则求完次幂后对第三个数取余
sum() 求和
min() 求最小值
max() 求最大值
"""

from itertools import product


number = '100'
print(int(number))  # 100
print(float(number))  # 100.0
print(bool(10))  # True

number = -10.58
print(abs(number))  # 10.58
print(round(number))  # -11
print(max(number,-9))  # -9

"""
列表和元组:
list() 将一个可迭代对象转换成列表
tuple() 将一个可迭代对象转成元组
reversed() 将一个序列翻转, 返回翻转序列的迭代器
slice() 列表的切片
"""
s = 'hello'
print(list(s)) # ['h','e','l','l','o']
st = "hello! I am Running"
s = slice(1, 10, 3)
print(st[s])    # eoI


"""
str () 将数据转换成字符串

format() 与具体数据相关,用于计算各种小数.精算等

memoryview() 查看bytes的内存中的情况

ord() 输入字符找带字符编码的位置

chr() 输入位置数字找对应的字符

ascii() 是sdcll码中的返回值 不是就返回u...
"""

# 找到对应字符的编码位置
print(ord('s'))  # 115
print(ord('宋'))  # 23435
# 找到对应编码位置的字符
print(chr(97))   # a
print(chr(20013))  # 嵩
# 在ascii中就返回这个值. 如果不不在就返回\u...
print(ascii('a'))  # 'a'
print(ascii('好'))   # '\u597d'


"""
数据集合:
dict() 创建一个字典
set() 创建一个集合
frozenset() 创建一个冻结的集合.冻结的集合不能进行添加和删除操作
"""

"""
其他相關：
len() 返回一个对象中的元素的个数
sorted() 对可迭代对象进行排序
enumerate() 获取集合的枚举对象
all() 可迭代对象中全部是True.结果才是True
any() 可迭代对象中有一个是True,结果就是Ture
zip() 函数用于将可迭代的对象最为参数.将对象中对应的元素打包成一个个元组
eval() 执行字符串类型的代码,并返回最终的结果
"""

lt = ["Song", "Running", "Ruby"]
for index, el in enumerate(lt):
  print(str(index)+"==>"+el)
    
# all() any()的使用
print(all([0,8,True,0]))
print(any([0,1,''])) 

# zip()使用
lt1 = [20,30,40]
print(zip(lt,lt1))

# eval()的使用
print(eval("2+2")) 
n = 6
print(eval("2+n")) 

"""
递归函數：
⼀个函数可以调⽤其他函数， 如果函数在内部调⽤其本身，这个函数就是递归函数。
构成递归不报错的话，严格来说应该具备两个条件:
1.从入口开始不断的向出口靠近
2.必须有出口的结束条件,即不递归的代码部分
"""
def digui(num):
    print(num)
    if num>0:
        digui(num-1)  # num-1 就是不断的向出口靠近,出口就是 num>0 的时候
    else:
        print('over')

digui(8)

# 理论上，所有的递归函数都可以写成循环的方式.比如求阶乘的代码
# 循環
def jiecheng1(num):
    product = 1
    for i in range(1,num+1):
        product = product * i
    return product
# 递归完成
def jiecheng2(num):
    if num == 1:
        return 1
    else:
        return num * jiecheng2(num - 1)
print(jiecheng1(4))
print(jiecheng2(4))

# 斐波那契数列 1+2+3+4+5+...
def func(n):
    # 给递归一个出口  第一位和第二位都是1
    if n == 1 or n == 2:
        return 1
    else:
        # 从第三位开始  返回上一个数加上上一个数
        return func(n-1) + func(n-2)
        
res = func(10)
print(res)

"""
匿名函数
变量名称 = lambda 参数：表达式
注意事项:
无需使用return返回,上述格式中冒号后面的内容即是要返回的
可以包含if... else等结构
"""
func = lambda a,b:a+b   # 定义匿名表达式
result = func(1,2)
print(result)  # 3

"""
高阶函数：
sorted()
max()
min()
map()
filter()
"""

"""
sorted(Iterable, key= None, reverse = False)
Iterable:排序规则(排序函数),在sorted内部会将可迭代对象中的每个元素传递给这个函数的参数.根据函数运算的结果进行排序
reverse:是否是倒序,  True:倒序  False:正序
key:就可以使用匿名函数
"""

# 按照年龄排序
dict1 = {'小红':20,'小明':18,'小鱼':19,'小雪':22,'小东':17}
order_dict = sorted(dict1.items(),key=lambda s:s[1])
print(dict(order_dict)) 
# order_dict 是一个列表[('小东', 17), ('小明', 18), ('小鱼', 19), ('小红', 20), ('小雪', 22)],所以需要转成字典

# 按照数量排序
goods = [('防脱发洗发水', 60, 3), ('格子衬衫', 156, 1), ('牛仔裤', 99, 7), ('运动鞋', 299, 2)]
goods = sorted(goods, key=lambda g: g[2], reverse=True)  # 设置成降序
print(goods)

# 最大值，最小值函数
result = max(dict1.items(),key=lambda s:s[1])
print(result)

result = min(dict1.items(),key=lambda s:s[1])
print(result)

"""
map(function,iterable)
map 映射函数,可以对可迭代对象中的每一个元素按照 function 的定义进行映射
有两个参数，第一个参数是一个函数，第二个参数是可迭代的内容
函数会依次作用在可迭代的每个内容上，返回一个新的可迭代内容
"""
list1 = [1, 2, 3, 4]
result = map(lambda x: x ** 2, list1)
print(result)  # 结果: [1,4,9,16]

# 或者也可以对两个列表进行映射
list2 = [5, 6, 7, 8, 9] 
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # 结果:[6,8,10,12]

"""
filter 函数 即筛选函数
语法: filter(function. Iterable)
function:用来筛选的函数,在filter中会自动的把iterable中的元素传递给function.
然后根据function返回的Ture或者False来判断你是否保留此项数据
iterable:可迭代对象
"""
list1 = [1, '3', 5, 'a', 'b', 'c', 7, 'u', 'y']
list2 = filter(lambda x: isinstance(x, int), list1)
print(list(list2))  # 结果:[1,5,7]

list3 = [1, 2, 4, 5, 8, 9, 0, 7]
list4 = filter(lambda x: x % 2 == 0, list3)
print(list(list4))  # 结果:[2,4,8,0]

