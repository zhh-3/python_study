# -*- codeing = utf-8 -*-
# @Time : 2021/4/13 16:06
# @Author : zhaha
# @File : no_3.py
# @Software : PyCharm


import json
class Employee(object):
    def __init__(self, empno, emname, salary):
        self.empno = empno
        self.emname = emname
        self.salary = salary

    def set_empno(self, empno):
        self.empno = empno

    def set_emname(self, emname):
        self.emname = emname

    def set_salary(self, salary):
        self.salary = salary


pno = input("员工编号:")
name = input("员工姓名:")
salary = input("员工工资:")
employee = Employee(pno, name, salary)

with open("E:\\employees.txt", 'w') as fp:
    json.dump({"pno": employee.empno, "name": employee.emname, "salary": employee.salary}, fp)
    print("保存完毕!")
    fp.close()
