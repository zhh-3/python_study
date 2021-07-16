import os
import time
print(os.getcwd())#输出当前路径
#修改当前路径
os.chdir('F:\\python\\')
print(os.getcwd())
#遍历当前路径下文件夹
print(os.listdir())
#创建新的文件夹
os.mkdir('F:\\pythoncode\\A')
os.mkdir('F:\\pythoncode\\B')

#删除文件
#os.remove('F:\\pythoncode\\A\\a.txt')

#删除文件夹,只能删除空文件夹
os.rmdir('F:\\pythoncode\\A')
os.rmdir('F:\\pythoncode\\B')

#操作系统
#os.system('cmd')  #唤醒虚拟机
#os.system('calc') #计算器

#本级目录
print(os.curdir)
print(os.listdir(os.curdir))

#改名os.rename(old name,new name)
#os.rename('A','B')

#os.path
#去除目录路径，分离出文件名
print(os.path.basename('E:\\wenjian\\abc\\d.txt'))
#去除文件名，分离出目录路径
print(os.path.dirname('E:\\wenjian\\abc\\d.txt'))
#组合成路径
print(os.path.join('A','B','C'))
print(os.path.join('E:\\','A','B','C'))
#分割文件名和路径，返回元组，完全使用目录，则最后一个作为文件名分离
a = os.path.split('E:\\wenjian\\abc\\d.txt')
print(a)
#分离文件名与扩展名
b = os.path.splitext('E:\\wenjian\\abc\\d.txt')
print(b)
#返回文件尺寸,单位是字节
c = os.path.getsize('E:\\wenjian\\abc')
print(c)
#返回文件最近访问时间，getatime
#返回文件创建时间，getctime
#返回文件最新修改时间，getmtime
#返回值为浮点型，可以用time模块中的gmtime()
d = time.gmtime(os.path.getctime('E:\\wenjian\\abc'))
e = time.localtime(os.path.getctime('E:\\wenjian\\abc'))
print(d)
print(e)

#判断指定路径是否存在   exists
#判断指定路径是否为绝对路径  isabs
#判断是否为目录  isdir
#判断是否为文件  isfile
#判断指定路径是否存在一个挂载点  ismount
#判断是否两个路径指向同一个文件  samefile(path1,path2)
