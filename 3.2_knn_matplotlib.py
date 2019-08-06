# coding=utf8
import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

# 中文顯示
import matplotlib.font_manager as fm
# 解決中文亂碼
myfont = fm.FontProperties(fname='C:\Windows\Fonts\kaiu.ttf')

'''創建數據源, 返回數據集和類標籤'''
def creat_dataset():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5]]) # 數據集
    labels = ['非常熱', '非常熱', '一般熱', '非常熱'] # 類標籤
    return datasets, labels

'''可視化分析數據'''
def analyze_data_plot(x, y):
    fig = plt.figure()
    # 將圖框劃分1行1列1塊
    ax = fig.add_subplot(111)
    ax.scatter(x, y)

    # 設置散點圖標題和橫縱坐標
    plt.title('遊客冷熱感知散點圖', fontsize=50, fontname='微軟正黑體', fontproperties=myfont) # Traveler Feeling Scatter
    plt.xlabel('冰淇淋數目', fontsize=10, fontname='微軟正黑體', fontproperties=myfont) # ice cream count
    plt.ylabel('喝水的數目', fontsize=10, fontname='微軟正黑體', fontproperties=myfont) # drink water count

    # 自動儲存圖表
    plt.savefig('dataset_plot.png', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    # 1.創建數據集和類標籤
    datasets, labels = creat_dataset()
    # print('Datasets:\n', datasets, '\nlabels:\n', labels)

    # 2.可視化分析數據
    analyze_data_plot(datasets[:, 0], datasets[:, 1])