# 格式化输出
'''
age = 18
print("我的年龄是:", age)
print("我的年龄是:%d" % age)
name = "hahn"
print("姓名：%s,我的国籍是%s" % (name, "中国"))

print("aaa", "bbb", "ccc")  # aaa bbb ccc
print("www", "baidu", "com", sep=".")
print("hello", end="")
print("world", end="\t")
print("python", end="\n")
print("end")
'''

password = input("请输入密码:")  # str类型
print("您的密码是：", password)
print(type(password))

# 装换数据类型
a = int(password)
b = a + 100
print("password+100=", b)

c = int(input("输入："))
print("输入了一个数字:%d" % c)
