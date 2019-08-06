# coding=utf8
import numpy as np
from numpy import *

'''創建數據源, 返回數據集和類標籤'''
def creat_dataset():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5]]) # 數據集
    labels = ['非常熱', '非常熱', '一般熱', '非常熱'] # 類標籤
    return datasets, labels

if __name__ == '__main__':
    datasets, labels = creat_dataset()
    print(datasets,'\n', labels)