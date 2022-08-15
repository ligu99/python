"""
class 类名:
属性
方法

注意：
1.类名的首字母要求大些，不要使用中文。
2.类名后面是有冒号的
3.类体像函数体一样需要缩进的
"""

from re import I


class Phone:
    brand = "iPhone"
    addr = "美国"
    date = "2022"
    def call(self):
        print("打电话")
    def send_msg(self):
        print("发信息")

"""
对象是具体的，类是抽象的
创建对象的方式：
对象名 = 类名([参数,...])
"""

iPhone6 = Phone()

"""
查看对象的属性和调用对象的动作:
对象名.属性名
或者
对象名.方法名()
"""
print(iPhone6.brand)

"""
对象属性添加/修改
1.对象.属性名=新值
2.__init__
"""
iPhone6.date = '2018'
iPhone6.price = '2000'
print(iPhone6.date,iPhone6.price)



class Person:
    country = '中国'
   
    # 定义__init__方法
    def __init__(self,name):
        print('我是一个__init__方法')
        print(self)
        self.name = name   # 此时就相当于在self这个空间中存放了一个name属性
     
    def eat(self):
        print('我是吃货，每天各种美食吃吃喝喝真美！')
     
# p = Person()  # 此时报错，没有参数  注释掉
p = Person('龟仙人')
print(p.name)


"""
面向对象类与对象的使用步骤：
1.提取特征、动作，定义类
2.在类中定义__init__方法初始化属性
3.在类中定义方法
4.根据类，创建对象
5.对象调用属性或者方法

"""

class Person:
    country = '中国'
   
    # 定义__init__方法
    def __init__(self,name):
        print('我是一个__init__方法')
        print(self)
        self.name=name
   
   # 此处再次强调self，self表示对象，谁调用eat此时的self就是谁 
    def eat(self):
        print(self.name + '是吃货，每天各种美食吃吃喝喝真美！')
   
    # 当然方法中也可以有更多的语句
    def sport(self,time):
        if time<6:
            print(self.name+'你太勤快了，起这么早去练功了啦！赞')
        else:
            print('怎么这么爱偷懒呢？还不抓紧时间练功去！哼！')
            # 比如练完功了，吃饭去,注意使用eat
            # self.eat() 

p = Person('悟空')        
p.eat()
p.sport(4)

p = Person('雅木茶')        
p.sport(9)