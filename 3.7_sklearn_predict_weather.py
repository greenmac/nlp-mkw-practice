# coding=utf8
import numpy as np
from numpy import *
from sklearn import neighbors

'''創建數據源, 返回數據集和類標籤'''
def creat_dataset():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5], [9, 4, 2], [7, 0, 1], [1, 5, 4], [4, 0, 5]]) # 數據集
    labels = [0, 0, 1, 1, 0, 0, 1, 1] # 類標籤,[0:'非常熱', 1:'一般熱']
    return datasets, labels

def knn_sklearn_predict(newV, datasets, labels):
    # 調用機器學習庫knn分類器算法
    knn = neighbors.KNeighborsClassifier()
    # 傳入參數, 特徵數據, 分類標籤
    knn.fit(datasets, labels)
    # knn預測
    predict_res = knn.predict([newV])
    print('該訪客認為天氣是:\t', '非常熱' if predict_res[0] == 0 else '一般熱')
    return predict_res

def predict_temperature():
    # 1.創建數據集和類標籤
    datasets, labels = creat_dataset()
    # 2.採訪新遊客
    iceCream = float(input('Q:請問你今天吃了幾個冰淇淋? \n'))
    drinkWater = float(input('Q:請問你今天喝了幾瓶(杯)水? \n'))
    playAct = float(input('Q:請問你今天戶外活動幾個小時? \n'))

    newV = array([iceCream, drinkWater, playAct])
    res = knn_sklearn_predict(newV, datasets, labels)



if __name__ == '__main__':
    predict_temperature()