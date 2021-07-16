# -*- codeing = utf-8 -*-
# @Time : 2021/4/18 0:53
# @Author : zhaha
# @File : no_3.py
# @Software : PyCharm


import matplotlib.pyplot as plt
import numpy as np

tick_label = ["5year", "10year", "20year", "50year", "100year"]
Freeze = [66386, 58230, 89135, 78415, 139361]
Wind = [174296, 381139, 80552, 81858, 331509]
Flood = [75131, 78045, 152558, 150656, 343164]
Quake = [577908, 99308, 497981, 193263, 731380]
Hail = [32015, 160454, 603535, 69638, 52269]
X = np.arange(len(Freeze))

bar_width = 0.15

for x, y in zip(X, Freeze):
    plt.text(x+0.005, y+0.005, '%d' % y, ha='center', va='bottom')

for x, y1 in zip(X, Wind):
    plt.text(x+0.2, y1+0.005, '%d' % y1, ha='center', va='bottom')

for x, y2 in zip(X, Flood):
    plt.text(x+0.4, y2+0.005, '%d' % y2, ha='center', va='bottom')

for x, y3 in zip(X, Quake):
    plt.text(x+0.57, y3+0.005, '%d' % y3, ha='center', va='bottom')

for x, y4 in zip(X, Hail):
    plt.text(x+0.7, y4+0.005, '%d' % y4, ha='center', va='bottom')

plt.bar(X, Freeze, bar_width, align="center", color="red", label="FreeZe", alpha=0.5)
plt.bar(X+bar_width, Wind, bar_width, color="green", align="center", label="Wind", alpha=0.5)
plt.bar(X+bar_width+bar_width, Flood, bar_width, color="blue", align="center", label="Wind", alpha=0.5)
plt.bar(X+bar_width+bar_width+bar_width, Quake, bar_width, color="purple", align="center", label="Wind", alpha=0.5)
plt.bar(X+bar_width+bar_width+bar_width+bar_width, Hail, bar_width, color="yellow", align="center", label="Wind", alpha=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title('information')
plt.xticks(X+bar_width, tick_label)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.show()
