for i in range(5):  # for(i = 0;i<5;i++)
    print(i, end=" ")
print()

for i in range(0, 12, 3):  # for(i = 0;i<12;i+=3)
    print(i, end=" ")
print()

for i in range(5, 0, -1):  # for(i = 5;i>0;i--)
    print(i, end=" ")
print()

name = "wuhan"
for c in name:
    print(c, end=" ")  # w u h a n
print()

name = "武汉"
for c in name:
    print(c, end=" ")  # 武 汉
print()

# 对元组
a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i], end=" ")
print()
