# coding=utf8
import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import math

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

'''構造KNN分類器'''
# def knn_Classifier(newV, datasets, labels, 2):
#     # 1.獲取新的樣本數據
#     # 2.獲取樣本庫的數據
#     # 3.選擇k值
#     # 4.計算樣本數據與樣本庫數據之間的距離
#     # 5.根據距離進行排序
#     # 6.針對k個點, 統計各個類別的數量
#     # 7.投票機制, 少數服從多數, 輸出類別
#     pass

'''歐式距離計算1:d^2=(x1-x2)^2+(y1-y2)^2'''
def ComputeEuclideanDistance(x1, x2, y1, y2):
    d = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
    return d

'''歐式距離計算2:d^2=(x1-x2)^2+(y1-y2)^2'''
def EuclideanDistance(instance1, instance2):
    length = len(instance1)
    d = 0
    for x in range(length):
        d += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(d)


if __name__ == '__main__':
    # 1.創建數據集和類標籤
    datasets, labels = creat_dataset()
    # print('Datasets:\n', datasets, '\nlabels:\n', labels)

    # 2.可視化分析數據
    # analyze_data_plot(datasets[:, 0], datasets[:, 1])

    # 3.1歐式距離計算1
    d1 = ComputeEuclideanDistance(2, 4, 8, 2)
    print('d1:', d1)

    # 3.2歐式距離計算2
    # d2 = EuclideanDistance([2, 4], [8, 2], 2)
    d2 = EuclideanDistance([2, 4, 4], [8, 2, 2])
    print('d2:', d2)

    # KNN分類器
    newV = [2, 4, 0]
    # knn_Classifier(newV, datasets, labels, 2)