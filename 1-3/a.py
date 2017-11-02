# Python file
# Name  :   a
# Create:   2017/11/02 14:07
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin

# mcv             mean corpuscular volume
# alkphos         alkaline phosphotase
# sgpt            alamine aminotransferase
# sgot            aspartate aminotransferase
# gammagt         gamma-glutamyl transpeptidase
# drinks          number of half-pint equivalents of alcoholic beverages drunk per day
# selector        field used to split data into two sets


from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas
from pandas import DataFrame
from numpy import mean, median, var, std
import statistics
from pylab import plot, show
import pylab as pl
import random
import math

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/bupa.data"
dataSet = pandas.read_csv(url, names=['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks', 'selector'])

dataSet1 = dataSet['mcv'].head(100)

# 随机将数据生成两个集合 方式：将该数组随机打乱顺序 再分成两个集合
random.shuffle(dataSet1)
data1 = pandas.DataFrame(dataSet1.head(50))
data2 = pandas.DataFrame(dataSet1.tail(50))

# 修正样本方差
s1_modified = float(data1.std())
s2_modified = float(data2.std())
s1_mean = float(data1.mean())
s2_mean = float(data2.mean())

# 方差未知但相等 均值之差的置信区间
# 推理公式 书上 P75-76
# 利用scipy 的 t f函数
loc_A = s1_mean - s2_mean
scale_A = math.sqrt((49 * s1_modified * s1_modified + 49 * s2_modified * s2_modified) / 98) * math.sqrt(
    1 / 48 + 1 / 48)

loc_B = 0
scale_B = (s1_modified * s1_modified) / (s2_modified * s2_modified)

print("均值差的95%置信区间：", stats.t.interval(0.95, 98, loc_A, scale_A))

print("方差比的95%置信区间：", stats.f.interval(0.95, 50-1, 50-1, loc_B, scale_B))
