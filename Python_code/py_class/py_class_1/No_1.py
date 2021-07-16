# -*- codeing = utf-8 -*-
# @Time : 2021/3/2 21:42
# @Author : zhaha
# @File : No_1.py
# @Software : PyCharm

year = input("year:")
month = input("Month(1-12):")
day = input("Day(1-31):")
Year = year
Month = ""
Day = day+"th"

if month=="1" or month=="01":
    Month = "January"
elif month=="2" or month=="02":
    Month = "February"
elif month=="3" or month=="03":
    Month = "March"
elif month=="4" or month=="04":
    Month = "April"
elif month=="5" or month=="05":
    Month = "May"
elif month=="6" or month=="06":
    Month = "June"
elif month=="7" or month=="07":
    Month = "July"
elif month=="8" or month=="08":
    Month = "August"
elif month=="9" or month=="09":
    Month = "September"
elif month=="10":
    Month = "October"
elif month=="11":
    Month = "November"
elif month=="12":
    Month = "December"
else:
    Month = "no"

print(Month+" "+Day+","+Year)