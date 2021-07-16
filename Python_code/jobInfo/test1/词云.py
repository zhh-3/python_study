# -*- codeing = utf-8 -*-
# @Time : 2020/10/17 18:16
# @Author : zhaha
# @File : 词云.py
# @Software : PyCharm


import wordcloud
import imageio

py = imageio.imread(r"ci.png");

wc = wordcloud.WordCloud(
    width=1000,  # 图片的宽
    height=700,  # 图片的高
    background_color='white',  # 背景颜色
    mask=py,
    font_path="C:/Windows/Fonts/simfang.ttf"
)

wc.generate()
wc.to_file(r"out.png")
