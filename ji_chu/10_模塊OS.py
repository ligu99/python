"""
os模块: 对操作系统进行一系列操作模块
"""
import os
#getcwd() 获取当前工作目录(当前工作目录默认都是当前文件所在的文件夹)
result = os.getcwd()
print(result)

# mkdir()  创建文件夹
os.mkdir('potter')

#listdir() 获取指定文件夹中所有内容的名称列表
result = os.listdir('./potter')
print(result)

# 删除一个文件
os.remove('文件名')  #删除一个文件

print(os.environ)  # 获取系统环境变量

#当然也可以使用 os.path 下面的各种操作,os.path 是 os 模块的子模块

# abspath()  将相对路径转化为绝对路径
path = './potter'#相对
result = os.path.abspath(path)
print(result)

# getsize()  获取文件的大小
path = './potter/harry.py'
result = os.path.getsize(path)
print(result)

#isfile() 检测是否是文件
path = './potter/harry.py'
result = os.path.isfile(path)
print(result)

#isdir()  检测是否是文件夹
result = os.path.isdir(path)
print(result)