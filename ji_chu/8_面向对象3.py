"""
property为“私有”属性提供读取和修改的方法
"""
class Child:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name
    
    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'
    
    @property
    def age(self):
        return self.__age


c = Child('王二狗', 20)
print(c.name, c.age)   
c.name = ''
print(c.name)  

c.age=22

"""
注意: name(self)是get方法，用@property装饰，第二个name(self, name)是set方法，
用@name.setter装饰，可以认为@name.setter是前一个@property装饰后的副产品。
"""

"""
@staticmethod(静态方法)、@classmethod(类方法)
"""

"""
使用场景：
当方法中 需要使用类对象 (如访问私有类属性等)时，定义类方法
类方法一般和类属性配合使用
"""
class Child:
    __type = "儿童"

    # 类方法，用classmethod来进行修饰
    @classmethod
    def get_type(cls):
        return cls.__type
print(Child.get_type())

"""
静态方法的特点：
需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）。
静态方法 也能够通过 实例对象 和 类对象 去访问。
"""
class Child:
    type = "儿童"

    def __init__(self):
        name = None

    # 静态方法    
    @staticmethod
    def introduce():  # 静态方法不会自动传递实例对象和类对象
        print("我是一位可爱的小baby.....")

child = Child()
child.introduce()    # 可以用 实例对象 来调用 静态方法
Child.introduce()    # 可以用 类对象 来调用 静态方法