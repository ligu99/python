"""
Python一切皆对象
"""
number = 10

# 声明 func 函数
def func():
 n = 10
 m = 5
 total = 0
 for i in range(n):
  total = i+m
 print(locals())

# 定义类
class Person:
 def __init__(self,name):
  self.name=name
  
 def __str__(self):
  return self.name

print(globals())
# 调用函数
func()

"""
LEGB
"""

#内置的 Builtin 

number = 10 #全局的 Global

# 声明 func 函数
def func():
 number = 100   #闭包的 Enclosing
 def inner_func():
  number = 1000 #局部的 Local
  print(number)
 # 调用 inner_func()函数
  inner_func()

# 调用外部函数
func()

"""
查找顺序:

以inner_func()内部的print(number)为例：

1.如果inner_func()函数内部有number这个变量，那么number这个变量就是局部的；

2.如果inner_func()函数内，没有这个变量，那么就会去找该函数外层的函数func()中有没有number这个变量，如果有，那么这个number就是闭包的；

3.如果外层函数func()中没有变量number，那么就会去最外层的全局变量找；

4.如果全局变量没有number，就去内置中找。

"""

"""
注意：
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问。
"""
a = 10
b = 8
if a>b:
 c = 5
 print(a+b+c) #23
else:
 print(a+b)

print(a,b,c) #10 8 5

"""
注意：
在函数的内部不可以直接修改全局变量的值,需要使用关键字 global 声明
同样在内层函数中也不能直接修改外层函数的变量需要加 nonlocal 声明。
"""
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num+=5   # 此处对全局变量进行修改了
    print(num)
fun1()
print(num)


num = 1
def func():
    print(num) # 1
    a = 10
    def inner_func():
        nonlocal a
        a+=5
        print(a)    # 15
    # 调用 inner_func 函数
    inner_func()
    print(a+num)    # 16
    
#调用 func
func()

"""
闭包
闭包条件
在一个外函数中定义了一个内函数。
内函数里运用了外函数的临时变量。
并且外函数的返回值是内函数的引用

一般情况下，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
就把这个临时变量绑定给了内部函数，然后自己再结束。
"""
# 闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer(a):
    b = 10
    # inner是内函数
    def inner():
        #在内函数中 用到了外函数的临时变量
        print(a+b)
    # 外函数的返回值是内函数的引用
    return inner

if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回给了demo变量
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里执行demo()就相当于执行inner()函数
    demo() # 15

def outer(a):
    b = 10
    # inner是内函数
    def inner(c):
        #在内函数中 用到了外函数的临时变量
        print(a+b+c)
    # 外函数的返回值是内函数的引用
    return inner

if __name__ == '__main__':
   
    demo = outer(5)
  # 下面是相同的 demo 函数,同一份闭包变量
    demo(5) 
    demo(6)

"""
闭包用途
1.装饰器！装饰器是做什么的？其中一个应用就是，我们工作中写了一个登录功能，
我们想统计这个功能执行花了多长时间，我们可以用装饰器装饰这个登录模块，
装饰器帮我们完成登录函数执行之前和之后取时间。

2.面向对象！经历了上面的分析，我们发现外函数的临时变量送给了内函数。
对象有好多类似的属性和方法，所以我们创建类，用类创建出来的对象都具有相同的属性方法。

3.实现单例模式！这也是装饰器的应用。
"""
