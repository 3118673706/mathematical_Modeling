# 灰色关联算法
# 灰色关联分析不仅能够用做关联分析，也能够用于评价。
import numpy as np
# data1为参考数列，data2为比较数列,返回各个描述变量的系数值
def Grey_Relational_Analysis(data1,data2):
    [m,n] = data1.shape
    data3 = np.zeros((m,n))
    for i in range(0,n):
        data3[:, i] = np.abs(data1[:, i] - data2[:, 1])
    d_max = erwei_Max(data3)
    d_min = erwei_Min(data3)
    a = 0.5  # 定义分辨系数
    # 计算灰色关联矩阵
    data4 = (d_min + a * d_max) / (data3 + a * d_max)
    xishu = np.mean(data4, axis=0)
    return xishu
#计算二维数组最大值
def erwei_Max(a):
    Max = a[0][0]
    for i in a:
        t = max(i)
        if t > Max:
            Max = t
    return Max
#计算二维数组最小值
def erwei_Min(a):
    Min = a[0][0]
    for i in a:
        t = min(i)
        if t < Min:
            Min = t
    return Min