f = open('a.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(':',1)
        if role == 'haha':
            boy.append(line_spoken)
        elif role == 'zhh':
            girl.append(line_spoken)
    else :
        file_name_boy = 'boy'+str(count)+'.txt'
        file_name_girl = 'girl'+str(count)+'.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

#保存最后一段对话
file_name_boy = 'boy'+str(count)+'.txt'
file_name_girl = 'girl'+str(count)+'.txt'

boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

boy = []
girl = []
count += 1
f.close()
