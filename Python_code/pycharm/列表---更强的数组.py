names = ['haha','zhh','zhang',3]
#添加元素  append  extend insert
#添加一个元素
print(len(names))  #4
names.append('hao')
print(len(names))  #5
#添加多个元素
names.extend([3,'en']) #参数是一个列表
print(len(names))
#插入一个元素
names.insert(0,'张')
print(len(names))
print(names[0])

#删除元素  remove del pop
#删除指定元素
names.remove('haha') #参数是列表中存在的，否则报错
print(len(names))    #['张','zhh','zhang','hao',3,3,'en']
#删除指定位置元素
print('第',2,'个元素是：',names[1]) #zhh
del names[1]
print('删除后，第2个元素是：',names[1]) #zhang
# del names   表示删除整个数组
# pop
# pop() 取出栈顶元素
#['张','zhang','hao',3,3,'en']
name = names.pop() #'en'
print(name,len(names))
#pop(i) 取出第i+1个元素
name = names.pop(1) #'zhang'
print(name,len(names))

#['张','hao',3,3]
#切片，分割，只拷贝，不删除原列表中的元素,没写的元素代表开头或结尾
names2 = names[1:3] #1是开始的下标,3是结束的下标+1
names3 = names[:3]
names4 = names[1:]
for name in names2:
    print(name,end = ' ')
print()
for name in names3:
    print(name,end = ' ')
print()
for name in names4:
    print(name,end = ' ')
print('\n'+str(len(names)))
