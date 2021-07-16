# -*- codeing = utf-8 -*-
# @Time : 2021/4/5 14:36
# @Author : zhaha
# @File : no_1.py
# @Software : PyCharm


import re

s = 'aaa       bb       c  d  e    fff    '
print(' '.join(s.split()))  # 直接使用字符串对象的方法
print(' '.join(re.split('[\s]+', s.strip())))  # 同时使用re中的函数和字符串对象的方法
print(' '.join(re.split('\s+', s.strip())))  # 与上一行代码等价
print(re.sub('\s+', ' ', s.strip()))  # 直接使用re模块的字符串替换方法
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)  # 使用search()方法返回的match对象
print(m)
print(email[:m.start()] + email[m.end():])  # 字符串切片
print(re.sub('remove_this', '', email))  # 直接使用re模块的sub()方法
print(email.replace('remove_this', ''))  # 直接使用字符串替换方法
