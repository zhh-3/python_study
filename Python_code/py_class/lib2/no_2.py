# -*- codeing = utf-8 -*-
# @Time : 2021/4/23 23:24
# @Author : zhaha
# @File : no_2.py
# @Software : PyCharm


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
large = 22
med = 16
small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
df = pd.read_csv("mpg_ggplot2.csv")
fig = plt.figure(figsize=(16, 10),
                 dpi=80,
                 facecolor='white')
grid = plt.GridSpec(4,
                    4,
                    hspace=0.5,
                    wspace=0.2)
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])
ax_main.scatter('displ',
               'hwy',
                s = df.cty*4,
               data = df,
               c = df.manufacturer.astype('category').cat.codes,
                cmap = 'tab10',
                edgecolors = 'gray',
                linewidths = 0.5,
                alpha = 0.9)
ax_right.hist(df.hwy,
             40,
             histtype = 'stepfilled',
             orientation = 'horizontal',
             color = 'deeppink')
ax_bottom.hist(df.displ,
              40,
              histtype = 'stepfilled',
              orientation = 'vertical',
              color = 'deeppink')
ax_bottom.invert_yaxis()
ax_main.set(title='Scatterplot with Histograms \n displ vs hwy',
            xlabel='displ',
            ylabel='hwy')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)
xlabels = ax_main.get_xticks().tolist()
ax_main.set_xticklabels(xlabels)
plt.show()
