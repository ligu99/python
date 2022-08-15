"""
模块
一个脚本(.py)文件就是一个模块
注意：
1、自定义模块的时候要注意命名的规范，使用小写，不要使用大写，不要使用中文，不要使用特殊字符等；
2、不要与内置模块冲突 比如：sys、random、time 等。
"""

# 系统的其他模块
import time
t1 = time.time()
print(t1)
print(time.ctime(t1))

from datetime import datetime

print(datetime.now())  # 获取格式好的时间和日期

import random

print(random.random())   # 0到1的随机小数，是一个float浮点数
print(random.randint(1,10))  # 1到10之间的随机整数
print(random.randrange(1,10)) # 1到10之间的随机数（记得range只有头没有尾巴）
names = ['赵丽颖','杨幂','迪丽热巴','高圆圆','刘诗诗']
# 随机选出一位美女
print(random.choice(names))