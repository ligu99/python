# 变量
name = 'Harry Potter'
age = 10

# 函数
def fight(tool=None):
    if tool:
        print('在魔法学校驾驶'+tool+'练习飞行课!')
    else:
        print('走到魔法学校,就会练习飞行课!')
      
# 类: 课程类
class Course:
    def __init__(self,name,c_list = []):
        self.name = name  # 学员名
        self.c_list = []  # 课程列表
  
    # 选修课  c_name 表示课程名
    def add_course(self,c_name):
        if c_name:
            self.c_list.append(c_name)
        else:
            print('选修课程不能为空哦!')
 
    # 取消选修课   
    def remove_course(self,c_name):
        if c_name:
            self.c_list.remove(c_name)
        else:
            print('选修课程不能为空哦!')   