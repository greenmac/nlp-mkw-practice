import jieba

str = '我在網路上課'
res = ' '.join(jieba.cut(str))
print(res)