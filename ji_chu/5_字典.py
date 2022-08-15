# 字典的声明：花括号或者大括号 即{}

dict = {} #空字典
print(type(dict))

dict1 = {'小宝':'13850501856','小鹏':'13900881234'}
print(dict1)

"""
獲取
字典名[key]的方式获取
字典名.get(key,defaultvalue)的方式获取
区别：如果key在字典中不存在的情况下。第一种方式报错，第二种方式不报错，而且还可以设置默认值
"""
print(dict1['小宝'])
print(dict1['小鹏'])
print(dict1.get('小宝'))
print(dict1.get('小鹏'))

# get方法的第一个参数是key，第二个参数是默认值，即没有找到对应的key，显示的内容。
print(dict1.get('小飞','不存在此数据'))  # 不存在此数据

"""
添加與修改
字典名[key] = 新值
"""
dict1['小飞'] = '18912346666'
print(dict1)

dict1['小鹏'] = '18988888888'
print(dict1)

"""
添加或者修改元素的不常用方法
setdefault(key, value): 该方法总能返回指定 key 对应的 value；
但是如果该 key-value 对不存在，则先为该 key 设置默认的 value，
然后再返回该 key 对应的 value，存在则直接返回key对应的value值

update(dict参数):可使用一个字典所包含的 key-value 对来更新己有的字典。
在执行 update() 方法时，如果被更新的字典中己包含对应的 key-value 对，
那么原 value 会被覆盖；如果被更新的字典中不包含对应的 key-value 对，
则该 key-value 对被添加进去。没有返回值。
"""
result1 = dict1.setdefault('小飞2','18912346666')
print(dict1)
print(result1)

result2 = dict1.update({'小战':'18912346666'})
print(dict1)
print(result2)

"""
删除元素
del 字典名[key] : 删除指定key的键值对
字典对象.pop(key) : 用于获取指定 key 对应的 value，并删除这个 key-value 对
字典对象.popitem() : popitem() 方法用于随机弹出字典中的一个 key-value 对
"""
del dict1['小战']
dict1.pop('小飞2')
dict1.popitem()
print(dict1)

"""
查找元素
使用关键字in 判斷是否存在
values() 判斷值是否存在
"""
if '小宝' in dict1:
  print('小宝在啊！')
else:
  print('怎么小宝丢了啊？')

if '13850501856' in dict1.values():
  print('嘻嘻！有这个号码太好了')
else:
  print('呜呜～～没有找到这个号码呢')

# 獲取所有的值
for value in dict1.values():
  print(value)

# 获取键的keys()
for key in dict1.keys():
  print(key)

# 获取键值对的items()
for key,value in dict1.items():
  print(key,value)