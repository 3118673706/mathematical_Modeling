'''
数据采用Z-score方法标准化
'''
from sklearn.preprocessing import StandardScaler


def Z_score_StandardData(data):
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)
    return data
