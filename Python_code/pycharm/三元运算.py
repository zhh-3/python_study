print("输入第一个数字")
a = int(input())
print("输入第二个数字")
b = int(input())
c = a if a>b else b # c = a>b?a:b
print("较大的数为：")
assert 4 > 3 #断言,不成立时会自爆，结束
print(c)
