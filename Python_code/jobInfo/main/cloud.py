# -*- codeing = utf-8 -*-
# @Time : 2020/10/17 23:23
# @Author : zhaha
# @File : cloud.py
# @Software : PyCharm


from wordcloud import WordCloud
from main import rinse_data
from imageio import imread

def make_cloud(job):
    color_mask = imread("ci.jpg")
    result = rinse_data.rinse(job)
    wc = WordCloud(
        width=1000,  # 图片的宽
        height=800,  # 图片的高
        background_color='black',  # 背景颜色
        collocations=False,
        max_words=100,
        # mask=color_mask,
        font_path="C:/Windows/Fonts/simfang.ttf"
    )

    wc = wc.generate(result)
    wc.to_file(job+"out.png")
