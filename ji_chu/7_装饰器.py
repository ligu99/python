import logging

def add(x,y):
 result = x+y
 print('求和结果是：'+str(result))
 logging.info("add is running")

 import logging

def record_log(func,*args,**kwargs):
    logging.warning("%s is running" % func.__name__)
    func(*args,**kwargs)

def add(x,y):
    result = x+y
    print('求和结果是：'+str(result))
 
def func1():
    print('我是func1函数')

# 调用add函数
record_log(add,1,2)

# 调用func1函数
record_log(func1)

"""
===================================================
"""
def logger(func):
 def wrapper(*args,**kwargs):
  print('准备调用函数:'+func.__name__)
  # 执行func
  func(*args,**kwargs)
  print('哈哈哈，我调用了'+func.__name__+'很棒吧！点赞！')
 return wrapper

# 有一个求和的函数,给其添加装饰器
# @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
@logger
def add(x,y):
 result = x+y
 print('求和结果是：'+str(result))

add(5,3)


# Mark1为托尼的装甲
def Mark1(func):
    print('我是一副帅气的铠甲...')
    # 变身
    def transform(*args, **kwargs): 
        print('我要变身喽!')
        print('我变成钢铁侠了') 
        return func(*args, **kwargs) 
    print('装甲穿好了!!')
    return transform 
  
@Mark1
def Tony():
    """我是大名鼎鼎的托尼"""
    print('我是斯塔克工业的CEO')

Tony()
"""
执行顺序：
1.加载 Mark1 和 Tony
2.Mark1 装饰 Tony,即调用函数 Mark1 并将 Tony 作为参数传到函数中
3.首先打印:我是一副帅气的铠甲...
4.然后加载:transform()函数
5.接下来打印:装甲穿好了!!
6.最后将transform函数的引用返出去,并将返回值赋值给 Tony 即:Tony = transform
7.调用 Tony (注意:此时调用的就是transform函数)
8.打印:
我要变身喽! 我变成钢铁侠了 我是斯塔克工业的CEO
这三句话.
"""
# 上面代码的基础上我们打印查看一下
print(Tony.__name__)
print(Tony.__doc__)
# 原函数的元信息不见了，可使用functools.wraps，wraps


