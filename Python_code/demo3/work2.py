# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 0:11
# @Author : zhaha
# @File : work2.py
# @Software : PyCharm

def writeGS(f, gu):
    try:
        f.write(gu)
    except Exception as result:
        print(result)


def CopyGS(f, g):
    try:
        str = f.readline()
        while len(str) != 0:
            g.write(str)
            str = f.readline()
    except Exception as result:
        print(result)


try:
    f = open("GuShi.txt", "w")
    str = """       什么诗
    白日依山尽，黄河入海流。
    欲穷千里目，更上一层楼。"""
    writeGS(f, str)
    f.close()
except Exception as result:
    print(result)

try:
    f = open("GuShi.txt", "r")
    copy = open("copy.txt", "w")
    CopyGS(f, copy)
    f.close()
    copy.close()
except Exception as result:
    print(result)
