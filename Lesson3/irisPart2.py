# Python file
# Name  :   irisPart2
# Create:   2017/10/31 15:20
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin

#    1. sepal length in cm (花萼长)
#    2. sepal width in cm（花萼宽）
#    3. petal length in cm (花瓣长)
#    4. petal width in cm（花瓣宽）

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas
from pandas import DataFrame
from numpy import mean, median, var, std
import statistics
from pylab import plot, show
import pylab as pl

# 选取s-length 以及 s-width 为两个总体

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
dataSet = pandas.read_csv(url, names=['s-length', 's-width', 'p-length', 'p-width', 'type'])

# print(dataSet.describe())
# print("--- --- ---")

dataLength = dataSet['s-length']
dataWidth = dataSet['s-width']
# print(dataLength.head(10))
# print(dataWidth.head(10))

meanLength = statistics.mean(dataLength)
meanWidth = statistics.mean(dataWidth)
print('Length mean:', meanLength, ' Width mean:', meanWidth)

sigmaLength = statistics.stdev(dataLength)
sigmaWidth = statistics.stdev(dataWidth)
print('Length sigma:', sigmaLength, ' Width sigma:', sigmaWidth)

