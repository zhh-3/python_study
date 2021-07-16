i = 0
while i < 5:
    print("第%d次循环" % (i + 1))
    print("i=", i)
    i += 1

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("sum =", sum)

# 扩展while
num = 1
while num < 5:
    print("aaa", "bbb", "ccc")
    num += 1
else:
    print(num, "小于或等于 5")

i = 1
while i < 5:
    if i == 2:
        continue
    else:
        print(i)
    i += 1  # 此处在continue后，不会被执行，程序死循环
