# info = {"name": "zhh", "age": 18}
# print(info["name"])
# print(info["age"])
# # 访问不存在的键,直接访问会报错
# # print(info["gender"])
# # 使用get方法，则不会报错
# # print(info.get("gender"))  # None
# # print(info.get("gender", "m"))  # m被设为默认值，无此key时，返回m
#
# # 增
# newID = input("请输入学号")
# info["id"] = newID
# print(info.get("id"))
#
# # 删 del clear
# # del 删除键值对
# print("删除前: %s" % info["name"])
# del info["name"]
# print("删除后: %s" % info.get("name", "无"))
#
# # clear  清空字典
# print(info)
# info.clear()
# print(info)
#
# # 查
info = {"name": "zhh", "age": 18, "id": "0121814"}
print(info.keys())  # 所有键
print(info.values())  # 所有值
print(info.items())  # 所有项目

for key in info.keys():
    print(key)
for key, value in info.items():
    print("key=%s  value=%s" % (key, value))

# 使用for循环，类似键值对
mylist = ["a", "b", "c"]
# 使用枚举 enumerate
for i, x in enumerate(mylist):
    print(i, x)