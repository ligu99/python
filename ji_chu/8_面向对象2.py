"""
私有化
私有化可以理解成是更深层次的封装了，
即只有类的内部方法才能访问私有化的属性和方法，
通过正常的方式是无法访问对象的私有化属性和方法
"""
class Child:
    def __init__(self,name):
        self.name=name # 非私有属性
        self.__toy = '乐高' # 私有属性，在名字的前面添加了双下划线__

    # 成员方法
    def sleep(self):
        print('我好困啊！我要睡觉....')

    # 私有方法:就是在方法名字的前面添加双下划线__
    def __play_toy(self):
        print(f'我的名字叫:{self.name}！我又可以玩我们的玩具啦！悄悄告诉你我的玩具是:{self.__toy}')

# 创建对象
c = Child('牛牛')
print(c.name)
c.sleep()

# 调用私有属性和方法会报错的
# print(c.__toy)
# c.__play_toy()

class Child:
    def __init__(self,name):
        self.name=name # 非私有属性
        self.__toy = '乐高' # 私有属性，在名字的前面添加了双下划线__

        # 成员方法
    def sleep(self):
        print('我好困啊！我要睡觉....')

    # 私有方法:就是在方法名字的前面添加双下划线__
    def __play_toy(self):
        print(f'我的名字叫:{self.name}！我又可以玩我们的玩具啦！悄悄告诉你我的玩具是:{self.__toy}')
  
    # 定义公有方法获取私有属性
    def get_toy(self):
        return self.__toy
  
    #定义公有方法对私有属性进行设置
    def set_toy(self,toy):
        security_toys = ['乐高','芭比娃娃','毛绒玩具'] 
        if toy in security_toys:
            self.__toy = toy
            # 因为赋值成功,所以在调用__play_toy的时候就会获取最新赋值后的玩具名称
            self.__play_toy()
        else:
            print('小朋友其他玩具不安全哦!')

# 创建对象
c = Child('牛牛')
print(c.get_toy())
c.set_toy('芭比娃娃')
print(c.get_toy())

c.sleep()