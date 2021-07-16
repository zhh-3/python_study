# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 18:26
# @Author : zhaha
# @File : no_1.py
# @Software : PyCharm


class Stock (object):
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_prePrice(self):
        return self.__previousClosingPrice

    def get_curPrice(self):
        return self.__currentPrice

    def set_prePrice(self, prePrice):
        self.__previousClosingPrice = prePrice

    def set_curPrice(self, curPrice):
        self.__currentPrice = curPrice

    def getChangepercent(self):
        dif = self.__currentPrice - self.__previousClosingPrice
        ratio = 100*dif/self.__previousClosingPrice
        return ratio

    def show(self):
        print("The symbol is :", self.__symbol)
        print("The Name is :", self.__name)
        print("The previousClosingPrice is :", self.__previousClosingPrice)
        print("The currentPrice is :", self.__currentPrice)
        print("The change of price's percent is :", str(round(self.getChangepercent(), 2))+"%")


stock = Stock("INTC", "Inter Corporation", 20.5, 20.35)
stock.show()