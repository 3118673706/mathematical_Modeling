# XGBOOST算法
from xgboost import XGBRegressor
'''
此函数传入参数后没有归一化操作，使用前需要先归一化操作
返回的预测值
'''
def XGBOOST(X_train,Y,X_test):
    model = XGBRegressor(learning_rate=0.01,
                         n_estimators=2800,
                         max_depth=12,
                         gamma=0.05,
                         min_child_weight=1,
                         seed=0,
                         subsample=0.8,
                         colsample_bytree=0.8,
                         reg_alpha=0,
                         reg_lambda=1)
    model.fit(X_train, Y)
    y = model.predict(X_test)
    return y