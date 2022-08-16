# 线性回归
'''

输入为训练值、结果、测试值
返回结果参数
'''
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler    #引入缩放的包
import numpy as np
def linearRegression(X_train,Y,X_test):
    # 归一化操作
    scaler = StandardScaler()
    scaler.fit(X_train)
    x_train = scaler.transform(X_train)
    x_test = scaler.transform(X_test)

    # 线性模型拟合
    model = linear_model.LinearRegression()
    model.fit(x_train, Y)

    result = model.predict(x_test)
    return result