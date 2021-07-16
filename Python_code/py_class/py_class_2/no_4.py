# -*- codeing = utf-8 -*-
# @Time : 2021/3/10 16:45
# @Author : zhaha
# @File : no_4.py
# @Software : PyCharm

import time
import os


ti1 = time.time()
for i in range(0, 10):
    os.system("cls")
    print("------------执行开始------------")
    ti2 = time.time()
    ti = ti2 - ti1
    j = (i+1)*10
    k = str(j)
    m = str(ti)[0:5]
    print(k+"%"+"["+"**"*(i+1)+"->]"+m+"s")
    time.sleep(1)

print("------------执行结束------------")
