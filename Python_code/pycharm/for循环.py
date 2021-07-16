name = ["你好","不好","haha"]
for i in range(3):
    print(i,len(name[i]))  #0 2   1 2    2  4
for i in range(2,5):
    print(i,end=',')  #2,3,4
print()
for i in range(1,10,2):
    print("第",i,"次")  #第1次 第3次 第5次 第7次 第9次
