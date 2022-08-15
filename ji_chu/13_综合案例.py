import random


# 定义函数，n表示随机数范围  score表示打中一次的分数
def isHit(n, score):
    # 保存记录积分
    record = 0
    # 使用for循环模拟打靶30次
    for i in range(30):
        r1 = random.randint(1, n)
        r2 = random.randint(1, n)
        if r1 == r2:
            record += score

    return record


print('------------欢迎来到：和平精英特训岛-----------')
solider_name = input('特种兵留下大名吧！')
while True:
    choice = input('请选择：1.室内靶场 2. 大乱斗')
    #  使用if...elif进行判断
    if choice == '1':
        print('请坐稳!传送点立马带你进入室内靶场')
        # 定义列表保存多个枪支供特种兵选择
        guns = ['AKM', 'VSS', 'M416', 'M249', 'AUG', 'M726', 'SCAR-L']
        for g in guns:
            print(g)
        gun = input('请选择枪支:')
        # 定义列表保存难度
        levels = ['EASY', 'NORMAL', 'HARD']
        for l in levels:
            print(l)
        level = input('请选择难度等级:')

        # 打靶比赛,
        if level == 'EASY':
            score = isHit(10, 5)
        elif level == 'NORMAL':
            score = isHit(20, 10)
        elif level == 'HARD':
            score = isHit(30, 15)
        else:
            print('没有此等级！')
            break
        print(f'训练完毕！{solider_name}使用{gun}枪在{level}级别获得分数：{score}')
        break
    elif choice == '2':
        print('请做好准备！你立刻会变成一只可爱的光子鸡喽')
        print(f'{solider_name}变成了一只小鸡仔，而且还拥有一把炮弹枪，真是美滋滋～～～射击模式开始')
        coins = 0  # 表示金币数
        level = 1  # 表示等级数
        # 计数器，记录击中的敌人个数
        count = 0
        # 定义击中的规则，如果仍然使用随机数，随机数在1-20之间，如果产生的随机数是5的倍数则表示击中
        while True:
            r = random.randint(1, 20)
            if r % 5 == 0:
                print('恭喜你击中敌人')
                # 拾取的金币数是即当前的随机数，等级越高，
                coins += r * level
                count += 1

            # 因为有4种等级，我们定义0-400 1级  400-900 2级  900-1900 3级  1900以上 4级
            if 400 >= coins >= 0:
                level = 1
            elif 900 >= coins > 400:
                level = 2
            elif 1900 >= coins > 900:
                level = 3
            else:
                print(f'你已经是无敌的小鸡仔,共击中{count}个敌人！不用训练了直接上战场吧！')
                break

        break
    else:
        print('输入有误呢！重新输入一次吧！')