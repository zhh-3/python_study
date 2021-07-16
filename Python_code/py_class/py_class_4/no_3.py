# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 19:44
# @Author : zhaha
# @File : no_3.py
# @Software : PyCharm


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


const = _const()
const.SLOW = 1
const.MEDIUM = 2
const.FAST = 3

class Fan(object):
    def __init__(self, speed = const.SLOW, radius = 5, color = "blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed;

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, on):
        self.__on = on

    def switch(self):
        self.__on = not self.__on

    def show(self):
        print("Speed:", self.__speed)
        print("Radius:", self.__radius)
        print("Color:", self.__color)
        print("On:", self.__on)


f1 = Fan(const.FAST, 10, "yellow")
f1.switch()
f2 = Fan(const.MEDIUM, 5, "blue")
print("风扇1")
f1.show()
print("风扇2")
f2.show()