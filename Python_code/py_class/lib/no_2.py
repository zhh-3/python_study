# -*- codeing = utf-8 -*-
# @Time : 2021/4/13 15:16
# @Author : zhaha
# @File : no_2.py
# @Software : PyCharm


import re
CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
CN_telecom = [133, 153, 180, 181, 189, 177, 1700, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

def check(phones):
    find = r'[0-9]+'
    lists = re.findall(find, phones)
    phone = ""
    for list in lists:
        phone += list
    print("识别号码为：", phone)
    if len(phone) >= 11:
        for num1, num2, num3 in zip(CN_mobile, CN_union, CN_telecom):
            num1 = str(num1)
            num2 = str(num2)
            num3 = str(num3)
            flag1 = phone.startswith(num1)
            flag2 = phone.startswith(num2)
            flag3 = phone.startswith(num3)
            if flag1:
                print("移动运营商")
                break
            if flag2:
                print("联通运营商")
                break
            if flag3:
                print("电信运营商")
                break
    else:
        print("输入错误")


phones = input("情输入电话号码:")
check(phones)