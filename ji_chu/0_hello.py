print('hello')

"""
多行注釋
"""

# 單行注釋

# 類型
a = 5
b = "5"
c = True

print(type(a))
print(type(b))
print(type(c))

# 類型轉換

# 轉換為整數
print(int("100"))  # 100 将字符串转换成为整数
print(int(100.99))  # 100 将浮点数转换成为整数
print(int(True))  # 1 布尔值True转换成为整数是 1
print(int(False))  # 0 布尔值False转换成为整数是 0

# 以下两种情况将会转换失败
'''
99.88 和 56ab 字符串，都包含非法字符，不能被转换成为整数，会报错
print(int("99.88"))
print(int("56ab"))
'''

# 使用int()函数进行类型转换时，还可以传入两个参数，第二个参数用来表示进制。
print(int("21", 8))  # 输出的结果是17.八进制的21,对应的十进制数字是17
print(int("F0", 16))  # 输出的结果是240.十六进制的F0,对应的十进制数字是240

"""
以下写法会报错。八进制里允许的最大值是7,所以 29 不是一个合法的八进制数
print(int("29",8))
"""

# 轉換為字符串
str1 = str(45)  # '45'

# 转换成为布尔值
print(bool(''))
print(bool(""))
print(bool(0))

#if 判斷
if a == 5 and b == "5":
    print("T")
else:
    print("F")

if a == 5 and b == "6":
    print("1")
elif c == True:
    print("2")
else:
    print("3")

"""
循環：
    -for
    -while
"""

print("循環-start")
i=1
while i<=50:
    if i%2 == 0:
        print(i) 
    i+=1
print("循環-end")

"""
j=3
while j>=1:
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
    if username == 'admin' and password == '123456':
        print('身份验证成功!')
        break
    else:
        print('身份验证失败!')
        j -= 1
        print(f'还有剩余{j}次机会')
"""

"""
for 临时变量 in 序列:
    循环满足条件时执行的代码
"""
for s in "hello":
    print(s)
"""
range配合for的使用
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
"""

for x in range(5):
    print(x)
for x in range(1,6):
    print(x)

for x in range(1,20,3):
    print(x)

ss = 'abcdefg'

for index in range(len(ss)):
    print(ss[index])
"""
break：表示跳出整个循环结构
continue：表示跳过本次循环后面的语句不执行，继续下一次循环
"""

"""
Python中可以用in和not in判断一个字符串中是否存在另外一个字符或字符串，in和not in运算通常称为成员运算，会产生布尔值True或False
"""
s1 = 'hello, world'
n = len(s1)
print('he' in s1) 
print(len(s1))

# 索引
print(s1[2],s1[0])

# 获取第一个字符
print(s1[0], s1[-n])
# 获取最后一个字符
print(s1[n-1], s1[-1])
