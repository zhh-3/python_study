# -*- codeing = utf-8 -*-
# @Time : 2020/9/29 13:20
# @Author : zhaha
# @File : testRE.py
# @Software : PyCharm


import re

# pat = re.compile("aa")
# str = "hello world i'am a hah"
# str2 = "aa num is aa"
# n = pat.search(str2)
# m = pat.search(str)

m = re.search("asc", "aasc")    # 前一个字符串是模板，后一个是被检测对象
print(m)  # <re.Match object; span=(1, 4), match='asc'>
# print(n)

print(re.findall("[a-z]+", "abcDafEghF"))   # ['abc', 'af', 'gh']

#            old  new      str
print(re.sub("a", "A", "aabbccddAA"))

name = "zhh is a people haha"
find = re.compile("zhh is a .* haha")
print(re.findall(find, name)[0])