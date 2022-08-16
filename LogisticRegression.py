from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
# from sklearn.cross_validation import train_test_split  # 0.18版本之后废弃
from sklearn.model_selection import train_test_split
import numpy as np

def logisticRegression(X_train,Y,X_test):
    # 划分为训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(X_train,Y,test_size=0.2)
    # 归一化
    scaler = StandardScaler()
    # scaler.fit(x_train)
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.fit_transform(x_test)

    # 逻辑回归
    model = LogisticRegression()
    model.fit(x_train, y_train)
    # 预测
    predict = model.predict(x_test)
    return predict