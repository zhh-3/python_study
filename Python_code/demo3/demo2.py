a = 100


def test1():
    # a = 300  # name 'a' is assigned to before global declaration：全局变量生命应在其实用之前
    global a  # 定义a 为全局变量,修改后，全局变量也被修改了
    print(a)
    a = 200
    print(a)


def test2():
    print(a)


test1()
test2()