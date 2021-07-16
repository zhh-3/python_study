# -*- codeing = utf-8 -*-
# @Time : 2020/10/29 7:19
# @Author : zhaha
# @File : Bar_pic.py
# @Software : PyCharm


from pyecharts.charts import Bar
from pyecharts import options
from main import rinse

def get_bar(job):
    # 1.准备数据
    data = rinse.rinse_data(job)
    cate = []
    data1 = []
    for item in data.keys():
        cate.append(item)
    for item in data.values():
        data1.append(item)

    # 2. 创建图表对象
    bar = Bar()

    # 3. 关联数据
    bar.add_xaxis(cate)    # 确定x轴上要显示的内容
    bar.add_yaxis('词数', data1)

    # 4. 设置图表
    # 全局设置
    bar.set_global_opts(
            # 设置标题信息
            title_opts=options.TitleOpts(title='工作要求统计', subtitle='TOP10要求'),
            # 显示工具箱
            toolbox_opts=options.ToolboxOpts())

    # 系列设置
    bar.set_series_opts(
            # 设置是否显示数值
            label_opts=options.LabelOpts(is_show=False),
            # 添加标记点
            markpoint_opts=options.MarkPointOpts(data=[
                options.MarkPointItem(type_='min', name='最小值'),
                options.MarkPointItem(type_='max', name='最大值')
            ]))


    # 5. 数据渲染 - 生成图表
    bar.render()


# get_bar("数据挖掘")