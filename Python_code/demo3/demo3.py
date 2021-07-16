# f = open("test.txt", "w")
#
# f.writelines("hello world\n")
# f.writelines("你好，python")
#
# f.close()

# f = open("test.txt", "r")
#
# content = f.read(5)
# print(content)
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
#
# f.close()

# f = open("test.txt", "r")
#
# contents = f.readlines()
# i = 1
# for content in contents:
#     print("%d:%s" % (i, content))
#     i += 1
#
# f.close()

import os

# os.rename("test.txt", "test1.txt")
# 创建文件夹
# os.mkdir("ha")
# 删除文件夹
# os.rmdir("ha")
# 获取当前目录
# print(os.getcwd())
# 修改默认目录
# os.chdir("../")
# 获取目录列表
# print(os.listdir("./"))

f = open("D://c.txt", "w")
f.write("This is a piece of code\n")
f.write("The\n")
f.write("And\n")
f.close()