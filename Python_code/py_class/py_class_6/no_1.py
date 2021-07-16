# -*- codeing = utf-8 -*-
# @Time : 2021/4/17 23:17
# @Author : zhaha
# @File : no_1.py
# @Software : PyCharm


import matplotlib.pyplot as plt

city = ["Bristol", "Cardiff", "Bath", "Liverpool", "Glasgow", "Edinburgh", "Leeds", "Reading", "Swansea", "Manchester"]
Population = [617280, 447287, 94782, 864122, 591620, 464990, 455123, 318014, 300352, 395515]
plt.scatter(city, Population)
plt.xlabel("城市", fontproperties="SimHei")
plt.ylabel("人口", fontproperties="SimHei")
plt.title("城市-人口关系", fontproperties="SimHei")
plt.show()

explode = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]
plt.axes(aspect=1)
plt.pie(Population, explode=explode, labels=city, labeldistance=1.1, autopct='%2.1f%%', shadow=True, startangle=90, pctdistance=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(-0.2, 1))
plt.show()