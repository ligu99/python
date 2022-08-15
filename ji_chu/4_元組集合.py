# 元组的声明使用的符号是: 小括号
sports1 = ()  #空元素
print(type(sports1)) # <class 'tuple'>

sports = ('足球','篮球','网球','乒乓球','排球')
print(sports) 
print(type(sports))
print(len(sports))

# 声明含有一个元素的元组时，必须要加【逗号】。
sports2 = ('足球',)

# 切片和索引
print(sports[1])
print(sports[-1])
print(sports[3])
print(sports[2:])
print(sports[:3])
print(sports[::2])
print(sports[::-1])
print(sports[-2::-1])

# 遍歷
for sport in sports:
    print(sport)


"""
集合
集合是一个可变容器，就是支持里面元素的变化
集合内的数据对象都是唯一的(不能重复)
集合是无序的存储结构,集合内的数据没有先后关系
集合是可迭代对象
集合的底层是字典结构
"""

# 空集合：
set = set()
# 有元素的集合：
set1 = {'足球','篮球','网球','乒乓球','排球','篮球' }
print(type(set1))
print(len(set1))  #同样适用len()获取长度
print(set1) # 注意里面只有一个篮球和网球，即不允许重复元素

"""
添加元素: set.add()
删除集合元素:set.pop() 与 set.remove()
pop(): pop会从集合中随机删除一个数
remove(): 删除指定元素，如果是不存在的元素会报错。
discard(): 与remove()类似，如果是不存在的元素不会报错。
"""
set1.add('冰球')
set1.pop()
set1.remove("篮球")

"""
集合的运算操作
交集:& 求两个集合中共同都有的元素
并集:| 将两个集合并在一起
差集:- 求当前与另一个集合不同的
交叉补集:^ 交叉补集会去掉共有的部分，只保留双方独有的部分
"""
set2 = {'乒乓球','排球','篮球','网球','冰球'}
set3 = {'乒乓球','排球','篮球','羽毛球'}
print(set3&set2)
print(set3|set2)
print(set3-set2)
print(set2-set3)
print(set2^set3)