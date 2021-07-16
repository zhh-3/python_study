#将第一个字母变成大写
str1 = 'abc'
str1 = str1.capitalize()
print(str1)  #Abc

#全部换成小写
str2 = 'ABCDef'
str2 = str2.casefold()
print(str2)  #abcded

#字符串居中，然后以空格填充
str3 = 'alfdjs'
str3 = str3.center(30)
print(str3)

#返回sub在字符串中出现的范围
str4 = 'aabbccdd'
num = str4.count('aa')
print(num)  #1
print(str4.count('c',1,4))  #0,有范围

#判断是否以xxx结尾
print(str4.endswith('dd')) #true
print(str4.endswith('cc',1,5))  #false有范围

#判断是否以xxx开头
str8 = 'zhanghaohan'
print(str8.startswith('zhang')) #True

#查找字符串
print(str4.find('bc'))  #3
print(str4.find('bd'))  #-1,表示没找到

#插入分割符
str5 = 'haha'
str5 = str5.join('1234')
print(str5)  #1haha2haha3haha4

#切割
str6 = 'haha zhh zhang'
print(str6.split())  #默认以空格切割
print(str6.split('h')) #设置以h来切割
str7 = """zhang\n
hao\n
han"""
print(str7.splitlines())


