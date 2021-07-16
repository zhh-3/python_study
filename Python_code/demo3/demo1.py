def printinfo():
    print("---" * 10)
    print("     python就是简洁")
    print("---" * 10)


def add2(a, b):
    c = a + b
    print(c)


def add2num(a, b):
    return a + b


# 返回多个值
def divide(a, b):
    shang = a // b
    yu = a % b
    return shang, yu


printinfo()
add2(11, 21)
result = add2num(11, 22)
print(result)
shang, yu = divide(5, 2)
print(shang, yu)