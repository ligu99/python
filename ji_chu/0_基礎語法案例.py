"""
擲骰子游戲
"""
import random

print("*"*30)
print("Welcome My Game")
print("*"*30)

username = input("請輸入用戶名：")
coins = 0

answer = input("是否加入游戲（yes/no）?")

# 加入游戲
if answer == "yes":
    print("進入游戲...")
    while True:
        num = int(input('%s！当前您的金币为%d！请充值(100块钱30币，充值必须是100的倍数)：' % (username,coins)))
        if num%100==0 and num>0:
            coins+=(num/100)*30
        else:
            print("充值失敗")
        
        ans = input("是否繼續充值（yes/no）?")
        if ans == 'no':
            break
    print("當前金幣：",coins)

    # 開始游戲
    print("一局扣除5金幣，馬上開始...")
    count = 0
    
    while True:
        ran1 = random.randint(1,6)
        ran2 = random.randint(1,6)

        coins-=5

        guess = input("買大買小：")

        #判断输赢 6  如果赢返3金币，玩5局送10个
        if ran1+ran2>6:
            print(str(ran1+ran2)+" 點，大")
        else:
            print(str(ran1+ran2)+" 點，小")
        if (ran1+ran2)>6 and guess=="大" or (ran1+ran2)<=6 and guess=="小":
            coins+=3
            print("恭喜，當前金幣",coins)
        else:
            print("很遺憾，當前金幣",coins)

        # 次數加1
        count+=1
        # 玩5局送10个
        if count%5==0:
            coins+=10
            print("玩5局送10个金幣，當前金幣",coins)
        # 是否繼續
        flag = input("繼續游戲（yes/no）?")
        if flag== "no" or coins<5:
            print("主動離開/金幣不足")
            break

# 退出游戲
else:
    print("下次再來")