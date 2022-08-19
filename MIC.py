'''
最大信息系数法MIC
计算MIC的得分
输入x为二维数据，y为一维的
返回值为x每一维的MIC得分
'''
from minepy import MINE
def MIC(x,y):
    score = []
    for i in range(x.shape[1]):
        mine = MINE(alpha=0.6, c=15)
        mine.compute_score(x[:, i], y)
        score.append(mine.mic())
    return score