"""
open() 函数:用于创建或打开指定文件，该函数的常用语法格式如下：
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
此格式中，用 [] 括起来的部分为可选参数，即可以使用也可以省略。其中，各个参数所代表的含义如下：

file_name：要创建或打开文件的文件名称，该名称要用引号括起来。需要注意的是：该文件名称可以是相对路径也可以是绝对路径。一般使用相对路径。

mode：可选参数，用于指定文件的打开模式。默认以只读（r）模式打开文件，也可以是写入(w)模式，追加(a)模式等，具体可以参照下面的表格。

buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区。

encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）

mode模式一览表：
模式	意义
r	只读模式打开文件，读文件内容的指针会放在文件的开头。
t	文本格式（默认的），不能单独使用，要与读写结合使用
b	二格式，不能单独使用，要与读写结合使用
rt	文本格式读取文件，读文件内容的指针位于文件的开头，一般用于文本文件。（等同于r，因为t是默认的，即文本格式）
rb	以二进制格式、采用只读模式打开文件，读文件内容的指针位于文件的开头，一般用于图片文件、音频文件等。
w	以只写模式打开文件，若该文件存在，打开时会清空文件中原有的内容，如果文件不存在则会创建文件。
wb	以二进制格式、只写模式打开文件，一般用于音频文件、图片文件等
a	以追加模式打开一个文件，对文件只有写入权限，如果文件已经存在，文件指针将放在文件的末尾（即新写入内容会位于已有内容之后）；反之，则会创建新文件。

默认值mode = "r"
"""
stream = open('electronic_sports.txt',mode='w')
records = ['4月01日 17:00  IG PK RA','4月02日 17:00  苏州LGN PK SN','4月03日 17:00  FPX PK RA','4月04日 17:00  SN PK 西安WE','4月05日 17:00  北京JDG PK FPX','4月06日 17:00  SN PK TES']
for record in records:
    stream.write(record+'\n')
stream.close()


"""
异常处理：
1.使用异常处理try...except...finally 搞定
    try:
    可能会有异常的代码
    except：
    发生异常的时候，才会执行的代码
    finally:
    无论是否存在异常都会执行的代码部分

2.使用 with
    with context as 变量: pass
    注意缩进，其中的context是一个表达式，返回的是一个对象，var用来保存context表达式返回的对象
"""

stream=None
try:    
    # 创建读文件的流对象    
    stream = open('file/electronic_sports.txt',mode='r')    
    content = stream.read()    
    print(content)
    stream.close()
except:    
    print('呀！有异常了，文件找不到！')
finally:
    if stream!=None:
        stream.close()

# with open('file/electronic_sports.txt',mode='r') as stream:    
#     content = stream.read()    
#     print(content)
# print(stream.colsed)

try:
    with open('1.txt',mode='r') as stream:     # 1.txt是存在的，里面的内容是：hello123456。
        content = stream.read(5)  # 读取5个字节的内容
        print(content)
        stream.seek(-3,0)  # 设置指针的偏移，第二个参数0表示从头开始，第一个参数-3表示向左数-3
        content = stream.read() 
        print(content) 
except:
    print('error')
    print(stream.closed)