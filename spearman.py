'''
斯皮尔曼相关性系数算法
在得到的p值中，如果p值大于0.05，则没有显著性差异，也就是说没有理由认为显著性差异存在，即没有相关性，如果p值小于0.05，我们可以认为存在显著性差异
'''
from scipy import stats
stats.spearmanr()