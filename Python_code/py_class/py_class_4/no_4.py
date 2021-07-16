# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 20:17
# @Author : zhaha
# @File : no_4.py
# @Software : PyCharm

import re
find = r'([0-9]*-[0-9]*)'
str = "Suppose my PhoneNo. is 0535-1234567, yours is 010-12345678, his is 025-87654321."
items = re.findall(find, str)
print(items)
