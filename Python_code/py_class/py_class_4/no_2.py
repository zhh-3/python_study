# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 19:11
# @Author : zhaha
# @File : no_2.py
# @Software : PyCharm


class Account(object):
    def __init__(self, id=0, balance=100, annuallnterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annuallnterestRate = annuallnterestRate/100

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annuallnterestRate(self):
        return self.__annuallnterestRate

    def show(self):
        print("id:", self.__id)
        print("balance:", self.__balance)
        print("MonthlyInterestRate :"+str(round(self.getMonthly_InterestRate()*100, 2))+"%")
        print("MonthlyInterest :", round(self.getMonthly_Interest(), 2))

    def getMonthly_InterestRate(self):
        return self.__annuallnterestRate/12

    def getMonthly_Interest(self):
        return self.__balance*self.getMonthly_InterestRate()

    def withdraw(self, money):
        if money > 0:
            self.__balance -= money
        else:
            print("error")

    def deposit(self, money):
        if money > 0:
            self.__balance += money
        else:
            print("error")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, Id):
        self.__id = Id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def annuallnterestRate(self):
        return self.__annuallnterestRate

    @annuallnterestRate.setter
    def annuallnterestRate(self, an):
        self.__annuallnterestRate = an

a = Account(122, 20000, 4.5)
a.withdraw(2500)
a.deposit(3000)
a.show()
