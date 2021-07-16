# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 20:27
# @Author : zhaha
# @File : no_5.py
# @Software : PyCharm


import re

find1 = r'([0-9]+)'
find2 = r'[A-Z]{2,10}'
find3 = r'[a-z]+'

sts = ["Mountain View,CA 94040", "Sunnyvale,CA", "Los Altos,94023", "Cupertino 95014", "Palo Alto CA"]

for i in range(len(sts)):

    item1 = re.findall(find1, sts[i])
    item2 = re.findall(find2, sts[i])
    item3 = re.findall(find3, sts[i])

    ss = ""
    if len(item3) > 0:
        ss += "城市名+"
    if len(item2) > 0:
        ss += "洲名+"
    if len(item1) > 0:
        ss += "ZIP编码"
    print(ss)