# coding=utf8
import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import math
import operator

# 中文顯示
import matplotlib.font_manager as fm
# 解決中文亂碼
myfont = fm.FontProperties(fname='C:\Windows\Fonts\kaiu.ttf')

'''創建數據源, 返回數據集和類標籤'''
def creat_dataset():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5]]) # 數據集
    labels = ['非常熱', '非常熱', '一般熱', '一般熱'] # 類標籤
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
def knn_Classifier(newV, datasets, labels):
    k = len(newV)
    # 1.計算樣本數據與樣本庫數據之間的距離
    sqrtDist = EuclideanDistance3(newV, datasets)
    # 2.根據距離進行排序, 按照列向量排序, argsort為索引值排列
    sortDisIndexs = sqrtDist.argsort(axis=0)
    # 3.針對k個點, 統計各個類別的數量
    classCount = {} # 統計各個類別分別的數量
    for i in range(k):
        # 根據距離排序索引值找到類標籤
        votelabel = labels[sortDisIndexs[i]]
        # 統計類標籤的鍵值對
        classCount[votelabel] = classCount.get(votelabel, 0)+1
    # 4.投票機制, 少數服從多數, 輸出類別
    # 對各個分類字典進行排序, 降序, itemgetter(1)按照value排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # print(newV, 'KNN投票預測結果是:', sortedClassCount[0][0])
    return sortedClassCount[0][0]

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

'''歐式距離計算3:d^2=(x1-x2)^2+(y1-y2)^2'''
def EuclideanDistance3(newV, datasets):
    # 1.獲取數據向量的行向量維度和列向量維度
    rowsize, colsize = datasets.shape
    # 2.各特徵向量間作差值
    diffMat = tile(newV, (rowsize, 1))-datasets
    # 3.對差值平方
    sqDiffMat = diffMat**2
    # 4.差值平方和進行開方
    sqrtDist = sqDiffMat.sum(axis=1)**0.5
    return sqrtDist

'''利用KNN分類器預測隨機訪客天氣感知度'''
def predict_temperature():
    # 1.創建數據集和類標籤
    datasets, labels = creat_dataset()
    # 2.採訪新遊客
    iceCream = float(input('Q:請問你今天吃了幾個冰淇淋? \n'))
    drinkWater = float(input('Q:請問你今天喝了幾瓶(杯)水? \n'))
    playAct = float(input('Q:請問你今天戶外活動幾個小時? \n'))

    newV = array([iceCream, drinkWater, playAct])
    res = knn_Classifier(newV, datasets, labels)
    print('該訪客認為天氣是:', res)



if __name__ == '__main__':
    # 1.創建數據集和類標籤
    # datasets, labels = creat_dataset()
    # print('Datasets:\n', datasets, '\nlabels:\n', labels)

    # 2.可視化分析數據
    # analyze_data_plot(datasets[:, 0], datasets[:, 1])

    # 3.1歐式距離計算1
    # d1 = ComputeEuclideanDistance(2, 4, 8, 2)
    # print('歐式距離計算1:', d1)

    # 3.2歐式距離計算2
    # d2 = EuclideanDistance([2, 4], [8, 2], 2)
    # d2 = EuclideanDistance([2, 4, 4], [7, 1, 1])
    # print('歐式距離計算2:', d2)

    # 3.3歐式距離計算3
    # d3 = EuclideanDistance3([2, 4, 4], datasets)
    # print('歐式距離計算3:', d3)

    # 4.1單實例構造KNN分類器
    # newV = [2, 4, 0]
    # res = knn_Classifier(newV, datasets, labels)
    # print(newV, 'KNN投票預測結果是:', res)

    # 4.2單實例構造KNN分類器
    # vecs = array([[2, 4, 4], [3, 0, 0], [5, 7, 2]])
    # for vec in vecs:
    #     res = knn_Classifier(vec, datasets, labels)
    #     print(vec, 'KNN投票預測結果是:', res)

    predict_temperature()
