
"""
while 和 for 與else：

while 判断条件:
  条件成立时，循环体代码
else:
  循环后，不符合循环条件执行的代码

for x in 序列：
   循环体代码 
else:
   循环完所有序列，执行的代码 
"""

for s in "hello":
  print(s)
else:
  print("循环完所有序列，执行的代码")

"""
在非死循环中，正常情况下else里的语句都是会被执行的
循环语句和else共同出现时，在循环语句里都会配合break语句来使用
"""

i = 0
while i <= 12:
    if i == 7:
        break
    i += 1
    print(i)
else:
    print('循环条件不成立时执行的代码')

"""
执行后发现 else語句 没有被执行，因为只要循环没有顺利完成，中间被break中断了则else里面的内容就不会执行。
"""

