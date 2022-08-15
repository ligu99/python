def use_magic():
  print('我会施展厉害的魔法!')

"""
模块的导入
1.import 导入
    import 模块名
使用方式：
    模块名.变量名
    模块名.函数名
    模块名.类
"""
import harry
# import  harry  as  hy 对模块重命名

# 使用变量 name
print(harry.name)

# 调用函数
harry.fight()

# 类对象的创建
c = harry.Course('哈利')
c.add_course('黑魔法防御术')
print(c.name)

"""
模块的导入
2.from...import 导入
    form 模块名 import 变量
    form 模块名 import 函数
    form 模块名 import 类名
    form 模块名 import 变量1,变量2,函数...
使用方式：
    模块名.变量名
    模块名.函数名
    模块名.类
"""


"""
包介绍和包的导入
包就是文件夹，但该文件夹下必须存在 _init_.py 文件
import 包名.模块名
from 包名.模块名 import 变量,函数...
使用：
包名.模块名.变量
"""