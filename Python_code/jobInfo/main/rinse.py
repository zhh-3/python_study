# -*- codeing = utf-8 -*-
# @Time : 2020/10/16 15:43
# @Author : zhaha
# @File : rinse.py
# @Software : PyCharm


import jieba.analyse

# 关键词生成
def rinse_data(job):
    fr = open(job + "demands.txt", 'r')
    fw = open(job+"关键词.txt", "w")
    result = fr.read()
    jieba.analyse.set_stop_words("停用词.txt")
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
    jieba.suggest_freq("本科", True)
    content = jieba.analyse.extract_tags(result, topK=10, withWeight=True)
    info = {}
    for item in content:
        i = int(item[1]*10000)
        info[item[0]] = i
        demand_weight = item[0]+"  \t**********"+str(i)
        fw.write(demand_weight+'\n')
    fr.close()
    fw.close()
    return info