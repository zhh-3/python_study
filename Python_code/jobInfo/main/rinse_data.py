# -*- codeing = utf-8 -*-
# @Time : 2020/10/14 17:02
# @Author : zhaha
# @File : rinse_data.py
# @Software : PyCharm


import jieba

def load_stop_word():
    fs = open("停用词.txt", 'r', encoding='utf-8')
    stop_word = []
    while True:
        stop = fs.readline()
        if len(stop) == 0:
            break
        stop = stop.replace("\n", "")
        stop_word.append(stop)
    fs.close
    return stop_word


# 数据清洗
def rinse(job):
    stop_words = load_stop_word()
    stop_words.append(' ')
    stop_words.append("\n")
    jieba.suggest_freq("大数据", True)
    jieba.suggest_freq("后端", True)
    jieba.suggest_freq("高并发", True)
    jieba.suggest_freq("物联网", True)
    jieba.suggest_freq("Spring Boot", True)
    jieba.suggest_freq("Spring Cloud", True)
    jieba.suggest_freq("算法", True)
    jieba.suggest_freq("数据挖掘", True)
    jieba.suggest_freq("机器学习", True)
    jieba.suggest_freq("产品经理", True)
    result = ""
    try:
        f = open(job+"demands.txt", "r")
        fw = open(job+"数据清洗.txt", 'w')
        try:
            while True:
                contents = f.readline()
                if len(contents) == 0:
                    break
                # s = "1. 本科及以上学历，计算机或相关专业，良好的编码和设计能力；"
                demands = contents[2:]
                des = jieba.lcut(demands, cut_all=False)
                # 写一行
                info = ""
                for de in des:
                    if de not in stop_words:
                        if len(de) > 1:
                            info = info + de + " "
                if len(info) > 1:
                    fw.write(info + "\n")
                    result = result + info
        finally:
            f.close()
            fw.close()
    except Exception as e:
        print(e)
    return result