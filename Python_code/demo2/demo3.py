"""
# find  in not in
movies = ["a", "b", "c", "d", "a", "e"]
for movie in movies:
    print(movie, end=" ")
print("\n"+"--"*15)
if "a" in movies:
    print("找到了")
else:
    print("没有该数据")

begin = 1
end = 5
print(movies.index("a", begin, end))
print(movies.count("a"), " ", movies.count("b"))  # 不是字符串的拼接方式
"""
a = [1, 4, 3, 2]
print(a)
a.reverse()  #反转
print(a)
a.sort()  # 排序，由小到大
print(a)
a.sort(reverse=True)  # 排序，降序
print(a)