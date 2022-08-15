"""
class 父类名: # 默认继承object，但是都是省略了object

......

class 子类名(父类名):

....
"""

# 单继承
"""
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def eat(self):
        print(self.name + "正在吃饭...")

class Student(Person):        
    def study(self):
        print('我要好好学习！')
"""


"""
构造方法的继承
父类__init__调用方式：
1.super(当前类名,self)._init_(实参列表)

2.super()._init_(实参列表)

3.父类名._init_(self,其它参数)
"""
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def eat(self):
        print(self.name + "正在吃饭...")

class Student(Person):  
    def __init__(self,name,clazz):
      # 调用父类的构造方法(3种实现方式)
        # super(Student,self).__init__(name)
        # super().__init__(name)
        Person.__init__(self,name)
        self.clazz = clazz
                
    def study(self):
        print(f'我在{self.clazz},我要好好学习！')


s = Student('大宝','一年级3班')
print(s)
s.eat()
s.study()
print(s.age)


# 方法的重写
class Student(Person):  
    def __init__(self,name,clazz):
        super().__init__(name)
        self.clazz = clazz
                
    def study(self):
        print(f'我在{self.clazz},我要好好学习！')
        
    # 重写eat方法
    def eat(self,food):
     # 此时可以调用父类原有的方法通过关键字super，然后再添加自己的代码
     super().eat()
     print(f'{self.name}最喜欢的食物是:{food}')

# 创建对象
s = Student('大宝','一年级3班')
s.eat("汉堡")


"""
继承注意事项：

并不是所有的都可以继承哦！私有的是继承不了的。即父类的私有属性和私有方法是无法继承的。

Python中的**super()**方法设计目的是用来解决多继承时父类的查找问题，所以在单继承中用不用 super 都没关系；但是，使用 super() 是一个好的习惯。一般我们在子类中需要调用父类的方法时才会这么用。

super()的好处就是可以避免直接使用父类的名字.主要用于多重继承
"""
class A:
    def m(self):
        print('A')
    
class B:
    def m(self):
        print('B')
    
class C(A):
    def m(self):
        print('C')
        super().m()
    
c = C()
c.m()
"""
这样做的好处就是：如果你要改变子类继承的父类（由A改为B），
你只需要修改一行代码（class C(A): -> class C(B)）即可，
而不需要在class C的大量代码中去查找、修改基类名，
另外一方面代码的可移植性和重用性也更高。
"""

"""
多继承
多继承就是一个子类可以继承多个父类。格式：
class 父类A:

......

class 父类B:

......

class 子类名(父类A,父类B,..): # 即可以通过逗号分隔跟多个父类

....

"""
class A:
    def m(self):
        print('A')
 
class B:
    def m(self):
        print('B')
  
class C:
    def print_c(self):
        print('CCC')
 
class D(A,B,C):
    def m(self):
        print('D')
        super().m()
 
d = D()
d.m()
d.print_c()
"""
对象d调用m()函数的时候，首先在当前类搜索是否存在m函数，如果存在则打印结果，不存在则去父类找。
那super().m()调用的时候搜索父类的顺序是什么呢？
是按照继承时括号里面父类的顺序依次查找是否存在，
所以先判断A类是否有m函数，有则调用，没有继续向下查找
"""