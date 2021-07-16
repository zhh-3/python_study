import pickle
#定义一个元组
my_list = [123,3.14,['another',33]]
#以二进制的形式打开一个文件
pickle_file = open('my_list.pkl','wb')
#将元组中的数据以二进制形式保存
pickle.dump(my_list,pickle_file)
#关闭
pickle_file.close()
#以二进制的形式打开一个文件
pickle_file = open('my_list.pkl','rb')
#将数据写入元组中
my_list2 = pickle.load(pickle_file)
print(my_list2)
[123, 3.14, ['another', 33]]
