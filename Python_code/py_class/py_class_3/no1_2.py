# -*- codeing = utf-8 -*-
# @Time : 2021/3/17 19:29
# @Author : zhaha
# @File : no1_2.py
# @Software : PyCharm


def make_shirt(size, string = "I love Python"):
    print("This T_shirt's size is " + size + ".And it print '" + string + "'")


size1 = "Big"
size2 = "Medium"
size3 = "Small"
make_shirt(size1)
make_shirt(size2)
make_shirt(size3, "I love java")