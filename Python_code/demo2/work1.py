products = [["iphone", 6888], ["xiaomi", 3888], ["MacPro", 9999], ["coffee", 30]]
print("------ 商品列表 ------")
i = 0
for goods in products:
    print(i, "\t", goods[0], "\t", goods[1])
    i += 1

shop = []
money = 0
str_num = input("（按‘q’退出）请输入商品编号：")
while str_num != 'q':
    if str_num.isdigit():
        num = int(str_num)
        if num < len(products):
            shop.append(products[num])
            money += products[num][1]
            print("已添加商品", products[num][0])
        else:
            print("无此编号")
    else:
        print("输入错误")
    str_num = input("（‘q’退出）请输入商品编号：")
print("------ 购物车 ------")
i = 0
for good in shop:
    print(i, "\t", good[0], "\t", good[1])
    i += 1
print("总价：", money)
