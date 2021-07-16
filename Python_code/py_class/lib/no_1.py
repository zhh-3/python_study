# -*- codeing = utf-8 -*-
# @Time : 2021/4/13 14:11
# @Author : zhaha
# @File : no_1.py
# @Software : PyCharm
import random

def ttd():
    i = random.randint(1, 6)
    return i

def getsize(lists):
    num = 0
    for list in lists:
        num += list
    return num

def game(a_money):
    print("-----------游戏开始------------------")
    select = input("0.small  1.big  2.退出\n请选择大小：")
    if select == '2':
        return "FFF"
    ss = "您还剩余:"+str(a_money)+"元。请输压金:"
    s_money = int(input(ss))
    if (select == "0" or select == "1") and s_money <= a_money:
        lists = []
        print("掷骰子结果：")
        for i in range(0, 3):
            t = ttd()
            print(t, end=" ")
            lists.append(t)
        num = getsize(lists)
        print("\n总点数:", num)
        if (select == "0" and num <= 10) or (select == "1" and num >= 11):
            print("你赢了")
            return s_money
        else:
            print("你好笨")
            return -s_money
    else:
        print("请正确输入")
        return 0


money = 1000
while money > 0:
    T = game(money)
    if T == "FFF":
        print("您还剩余:" + str(money) + "元")
        break
    money += T
    print("您还剩余:"+str(money)+"元")