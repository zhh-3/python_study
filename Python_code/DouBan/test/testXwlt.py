# -*- codeing = utf-8 -*-
# @Time : 2020/9/29 15:02
# @Author : zhaha
# @File : testXwlt.py
# @Software : PyCharm


import xlwt

# 创建Workbook对象，既是excel表格
excel = xlwt.Workbook(encoding="utf-8")

# 创建一个表单
sheet = excel.add_sheet("sheet1")

# 写入数据
for i in range(0, 9):
    for j in range(0, i+1):
        sheet.write(i, j, '%d*%d=%d' % (i+1, j+1, (i+1)*(1+j)))
excel.save("99.xls")