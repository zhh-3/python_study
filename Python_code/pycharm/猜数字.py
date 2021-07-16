import random
num = random.randint(1,10)
print("------我在学python-------")
i = 1
temp = input("第"+str(i)+"次猜测")
guess = int(temp)
while guess != num and i <= 3:    
    print("猜错了")
    if guess > num:
        print("大了！大了！")
    else:
        print("小了！小了！")
    print("-------------------------")
    i = i+1
    if i <= 3:
        temp = input("第"+str(i)+"次猜测")
        guess = int(temp)
if i <= 3:
    print("猜对了")
    print("可惜没奖励")
print("游戏结束")
