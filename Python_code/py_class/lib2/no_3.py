# -*- codeing = utf-8 -*-
# @Time : 2021/4/24 10:59
# @Author : zhaha
# @File : no_3.py
# @Software : PyCharm

import matplotlib.image as mping  # mping用于读取图片
from pylab import *
import pandas as pd
from tqdm import tqdm


def draw_trend_chart(x, y):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.figure()
    plt.plot(x, y, "r", linewidth=1)
    plt.xlabel("DATE")  # x轴标签
    plt.ylabel("PRICE")  # y轴标签
    plt.title("STOCK")  # 标题
    plt.savefig("1.png")  # 保存图片名称
    lena = mping.imread('1.png')  # 读取图片文件信息
    #lena.shape  # （512,512,3）
    plt.imshow(lena)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.title("")
    plt.show()  # 显示


def get_weight_data(filename):
    time = []
    price = []
    raw_data = pd.read_csv(filename, header=None, encoding='utf-8')
    for year, yearmonthf, monthf, week, monthweek, weekdayf, VIX_Close in tqdm(raw_data.values):
        time.append(yearmonthf)
        price.append(VIX_Close)
    return [time, price]


raw_data = pd.read_csv("yahoostock.csv", header=None, encoding='utf-8')
i = 0
D = []
for year, yearmonthf, monthf, week, monthweek, weekdayf, VIX_Close in tqdm(raw_data.values):
    if i == 0:
        i = i + 1
        continue
    else:
        L = [year, monthf, monthweek, weekdayf, VIX_Close]
        D.append(L)
Year = []
for date in D:
    if date[0] not in Year:
        Year.append(date[0])
AveragePrice = []
for year in Year:
    i = 0
    k = 0
    for date in D:
        if date[0] == year:
            k = k + 1
            i = i + float(date[4])
    averageprice = i / k
    AveragePrice.append(averageprice)
print(AveragePrice)
MaxPrice = 0
DayOfMax = []
for date in D:
    if float(date[4]) > MaxPrice:
        MaxPrice = float(date[4])
        DayOfMax = date
print(str(DayOfMax[0]) + '-' + str(DayOfMax[1]) + '-' + str(DayOfMax[2]) + '-' + str(DayOfMax[3]))
data = get_weight_data("yahoostock.csv")
draw_trend_chart(data[0], data[1])
