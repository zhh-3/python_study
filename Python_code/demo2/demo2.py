"""
testlist = [1, "test"]
print(type(testlist[0]))
print(type(testlist[1]))

print(testlist[0])
print(testlist[1])

namelist = ["张", "王", "李"]
print("--"*10)
for name in namelist:
    print(name)
# 增加
# append 在末尾添加数据
nametemp = input("新的姓：")
namelist.append(nametemp)
print("--"*10)
for name in namelist:
    print(name)

a = [1, 2]
b = [3, [4, 5]]
a.append(b)
print(a)  # [1, 2, [3, [4, 5]]]
a.extend(b)  # [1, 2, [3, [4, 5]], 3, [4, 5]]
print(a)
"""
a = [1, 2, 3, 4]
index = 1
value = 5
a.insert(index, value)  # [1, 5, 2, 3, 4]
print(a)

# 删除 del  .pop  .remove
movies = ["a", "b", "c", "d", "a", "e"]
for movie in movies:
    print(movie, end=" ")
print("\n"+"--"*15)
# 指定下标删除
del movies[1]
for movie in movies:
    print(movie, end=" ")
print("\n"+"--"*15)
# 最后一个元素
movies.pop()
for movie in movies:
    print(movie, end=" ")
print("\n"+"--"*15)
# 第一个“a”
movies.remove("a")
for movie in movies:
    print(movie, end=" ")
print("\n"+"--"*15)