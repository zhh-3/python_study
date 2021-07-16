import random
a = 4
while a != 3:
    print("(0.剪刀)(1.石头)(2.布)(3.结束)")
    y = (input("请输入你的选择："))
    if y.isdigit():
        a = int(y)
        flag = True

        if 0 <= a <= 2:
            x = random.randint(0, 2)
            print("系统的选择", end=":")
            if x == 0:
                print("剪刀")
            elif x == 1:
                print("石头")
            else:
                print("布")

            if a == x:
                print("平局")
            else:
                if a == 0:
                    if x == 1:
                        flag = False
                    else:
                        flag = True
                elif a == 1:
                    if x == 0:
                        flag = True
                    else:
                        flag = False
                elif a == 2:
                    if x == 0:
                        flag = False
                    else:
                        flag = True
                if flag:
                    print("你赢了")
                else:
                    print("你输了")
        elif a == 3:
            print("游戏结束")
        else:
            print("没有该选项")
        print()
    else:
        print("请输入数字")
        print()