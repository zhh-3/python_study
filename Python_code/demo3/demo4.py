# -*- codeing = utf-8 -*-
# @Time : 2020/9/27 23:44
# @Author : zhaha
# @File : demo4.py
# @Software : PyCharm

# f = open("123.txt")  # 报错FileNotFoundError
"""
try:
    f = open("123.txt", "r")
except FileNotFoundError:
    pass

try:
    print(num)
except NameError:
    print("错误")
"""

"""
try:
    f = open("123.txt", "r")
    print(num)
except (FileNotFoundError, NameError):  # 有多个可能报错，用（）括起来
    print("有错误")
"""

# try:
#     f = open("123.txt", "r")
#     print(num)
# except Exception as result:  # result作为捕获结果
#     print("有错误呀")
#     print(result)
import time

try:
    f = open("test1.txt", "r")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件已关闭")
except Exception:
    print("发生异常")
