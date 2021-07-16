# -*- codeing = utf-8 -*-
# @Time : 2021/5/4 10:10
# @Author : zhaha
# @File : config.py
# @Software : PyCharm


import os

# 指定数据集路径
dataset_path = 'data'

# 结果保存路径
output_path = 'output'

if not os.path.exists(output_path):
    os.mkdir(output_path)


countries = ['CA', 'DE', 'GB', 'US']

# 使用的列
usecols = ['video_id', 'trending_date', 'channel_title', 'category_id', 'publish_time', 'views', 'likes',
         'dislikes', 'comment_count', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed']

'''
video_id: 视频id，字符串
trending_date: 视频上榜的日期，字符串
title: 视频标题，字符串
channel_title: 所属频道标题，字符串
category_id: 所属类别编号，整型
publish_time: 视频发布时间，时间类型
tags: 视频标签，字符串
views: 观看次数，整型
likes: 点赞次数，整型
dislikes: 被踩次数，整型
comment_count: 评论次数，整型 
comments_disabled: 评论是否关闭，布尔值 
ratings_disabled: 打分是否关闭，布尔值 
video_error_or_removed: 视频出错或者被删，布尔值 
description: 视频详情，字符串
'''
