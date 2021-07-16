while True:
    score = int(input("请输入成绩:"))
    if score <= 100: #大判断
        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        elif score >= 70:
            print("C")
        elif score >= 60:
            print("D")
        elif score >= 0:
            print("E")
        elif score == -1:
            break
        else:
            print("输入错误")
    else:
        print("输入错误")
