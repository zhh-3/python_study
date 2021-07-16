"""
if True:
    print("True")
else:
    print("False")

if 0:
    print("True")
else:
    print("False")
"""

score = int(input("输入成绩"))
if 100 >= score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("E")