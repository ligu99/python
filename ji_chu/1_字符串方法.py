"""
大小写相关操作
capitalize(): 字符串首字母大写
title(): 字符串中每个单词首字母大写
upper(): 字符串全部大写
lower(): 字符串全部小写
"""
s1 = 'hello, world!'
s = s1
# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())   # Hello, world!
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())        # Hello, World!
# 使用upper方法获得字符串大写后的字符串
print(s1.upper())        # HELLO, WORLD!

s2 = 'GOODBYE'

# 使用lower方法获得字符串小写后的字符串
print(s2.lower())        # goodbye


"""
查找
find(): 从字符串中查找另一个字符串(参数)所在的位置，如果存在则返回匹配的字符串的首字母下标，没有找到则返回-1
index(): 与find方法类似,如果找不到则会引发异常。
"""
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('good'))      # -1
print(s.index('or'))       # 8
# 找不到引发异常
# print(s.index('good'))     # ValueError: substring not found


"""
查找
rfind(): “r”表示的是right右侧，表示从右侧开始查找字符串,没有找到返回-1
rindex(): 与rfind方法类似，如果找不到则会引发异常
"""
# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 8
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 8


"""
判断
startswith():判断字符串是否以指定的字符串开头，返回布尔值结果
endswith()：判断字符串是否以指定的字符串结尾，返回布尔值结果
isdigit()：判断字符串是否由数字构成，返回布尔值结果
isalpha()：判断字符串是否以字母构成，返回布尔值结果
isalnum()：判断字符串是否以数字和字母构成，返回布尔值结果
"""

# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!'))       # True

s3 = 'abc123456'

# isdigit方法检查字符串是否由数字构成返回布尔值
print(s3.isdigit())    # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s3.isalpha())    # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s3.isalnum())    # True

# 去除空格
s4 = '   helloworld@126.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s4.strip())    # helloworld@126.com

"""
格式化字符串
字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。
"""
# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~

#數字格式化
a = 3
b = 4
print('%d * %d = %d' % (a, b, a * b))
# 字符串的方法来完成字符串的格式
print('{0} * {1} = {2}'.format(a, b, a * b))
# 更簡單的方法
print(f'{a} * {b} = {a * b}') #在这种以f打头的字符串中，{变量名}是一个占位符，会被变量对应的值将其替换掉

