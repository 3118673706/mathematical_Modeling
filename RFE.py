'''
递归特征消除法RFE（基于randforest)
输入x为二维数据,y为一维
输出rfe对象
'''
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
def REF_baseOnRandForest(x,y):
    rf = RandomForestRegressor(n_estimators=20, max_depth=4)  # 随机森林
    rfe = RFE(estimator=rf, n_features_to_select=1, step=1)
    rfe.fit(x, y)
    return rfe