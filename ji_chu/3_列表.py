heros = ['探险家','河流之王','荒漠屠夫','齐天大圣','冰晶凤凰','赛恩']
print(heros,type(heros))

"""
切片
列表名[start：end：step]
start和end是左闭右开的区间，step表示的是步长，并且步长可以是正向（从左向右）也可以是逆向（从右向左）取元素。
step如果是负数表示的是逆向，如果是正数表示的是正向
如果end省略则表示到列表最后一个元素，如果start省略表示从第一个元素开始
"""
# 打印：'河流之王','荒漠屠夫','齐天大圣'
print(heros[1:4])
# 打印：'河流之王','齐天大圣','赛恩',
print(heros[1::2])
# 打印：'赛恩','冰晶凤凰','齐天大圣'
print(heros[-1:2:-1])
# 打印: '冰晶凤凰','河流之王'
print(heros[-2::-3])


for h in heros:
    print(h)

print(len(heros))  # 长度为6



"""
增加/刪除
list.append(obj): 在列表末尾添加新的对象
list.extend(seq): 在列表末尾一次性追加另一个序列中的多个值
del list[索引] 表示 删除指定索引位置的元素
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并返回该元素的值,当然也可以索引值，表示 删除指定索引位置的元素跟del list[索引] 类似，但是这个pop有返回值，即被删除的元素
list.remove(obj) 移除列表中某个值的第一个匹配项，没有返回值
"""
# 使用append添加元素
heros.append('牛头酋长')
print(heros)
# 有一个新的heros列表
new_heros=['希维尔','崔斯特']
# 将new_heros添加到heros中
heros.extend(new_heros)
print(heros)

# 删除下标为1的元素
del heros[1]
print(heros) 
# 删除下标为1的元素，并获取返回值
element = heros.pop(1)
print(heros) 
print(element)
# 删除：'冰晶凤凰'
element2 = heros.remove('冰晶凤凰')
print(heros)
print(element2)
# 注意这句话会报错的，ValueError: list.remove(x): x not in list
# element3 = heros.remove('冰晶凤凰1')
# print(heros)


"""
修改元素
直接使用list[索引]进行替换
使用insert('元素名')
"""
# 使用列表方式替换原有元素
heros[0]='希维尔'
print(heros)

heros[-1]='牛头酋长'
print(heros)

# 使用insert指定索引位置替换
heros.insert(3,'崔斯特')
print(heros)

"""
查找
list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list.count(obj) 统计某个元素在列表中出现的次数
obj in list 其实这个在前面说过，但是也可以用于判断
"""

# 判断'荒漠屠夫'是否在列表中存在
n = heros.index('荒漠屠夫')
print(n)

# 判断'牛头酋长'是否在列表中存在 如果查找的元素不在列表中，会报错的，ValueError: '牛头酋长' is not in list。
# n = heros.index('牛头酋长')
# print(n)

# 也可以使用count判断个数
n = heros.count('冰晶凤凰')
print(n)

# 当然也可以使用：'荒漠屠夫' in heros
print('荒漠屠夫' in heros)

"""
其他操作
list.reverse() 反向列表中的元素
list.sort(cmp=None, key=None,reverse=False) 对原列表进行排序
"""
# 倒序列表中的元素
heros.reverse()
print(heros)

# 对列表中的元素进行排序
heros.sort()
print(heros)

# 对列表中的元素进行排序，也可以降序
heros.sort(reverse=True)
print(heros)