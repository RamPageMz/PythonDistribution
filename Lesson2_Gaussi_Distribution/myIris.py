# Python file
# Name  :   myIris
# Create:   2017/10/29 15:50
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

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
dataSet = pandas.read_csv(url, names=['s-length', 's-width', 'p-length', 'p-width', 'type'])

print(dataSet.describe())
print("--- --- ---")


def Gauss(typeName):
    dataSet1 = dataSet[dataSet['type'] == typeName]
    mu = statistics.mean(dataSet1['s-length'])
    sigma = statistics.stdev(dataSet1['s-length'])
    print(typeName, " s-length 均值和方差：")
    print(mu)
    print(sigma)
    x = np.linspace(mu - 5 * sigma, mu + 5 * sigma)
    y = stats.norm.pdf(x, mu, sigma)
    plt.plot(x, y, color='blue')
    plt.title('Gauss: $\mu$=%.2f, $\sigma^2$=%.2f' % (mu, sigma))
    plt.xlabel('sepal length')
    plt.ylabel('Probability density')
    plt.show()


Gauss("Iris-setosa")

dataSet1 = dataSet[dataSet['type'] == 'Iris-setosa']
df1 = pandas.DataFrame(dataSet1)
dataSet2 = dataSet[dataSet['type'] == 'Iris-versicolor']  # Iris-virginica
df2 = pandas.DataFrame(dataSet2)
dataSet3 = dataSet[dataSet['type'] == 'Iris-virginica']
df3 = pandas.DataFrame(dataSet3)

df = pandas.DataFrame(dataSet)

# df4 = pandas.DataFrame(dataSet)
# df4.plot.hist(alpha=0.5)
# plt.show()

# dataType1 = dataSet[dataSet['type'] == 'Iris-setosa']
# print(dataType1.shape)
#
# df = pandas.DataFrame(dataType1)
# df = df.cumsum()
# df.plot()
# plt.show()

# 盒子图
df1.plot.box()
plt.show()

# 三种亚种比较
plt.subplot(2, 2, 1)
plot(df1['s-length'], df1['s-width'], 'b+', label='Iris-setosa')
plot(df2['s-length'], df2['s-width'], 'r+', label='Iris-versicolor')
plot(df3['s-length'], df3['s-width'], 'g+', label='Iris-virginica')
plt.legend(loc='upper left')
# plt.title("sepal length & sepal width")  # petal
plt.xlabel('sepal length')
plt.ylabel('sepal width')
# show()

plt.subplot(2, 2, 2)
plot(df1['s-length'], df1['p-length'], 'b+', label='Iris-setosa')
plot(df2['s-length'], df2['p-length'], 'r+', label='Iris-versicolor')
plot(df3['s-length'], df3['p-length'], 'g+', label='Iris-virginica')
plt.legend(loc='upper left')
# plt.title("sepal length & petal length")  # petal
plt.xlabel('sepal length')
plt.ylabel('petal length')
# show()

plt.subplot(2, 2, 3)
plot(df1['s-length'], df1['p-width'], 'b+', label='Iris-setosa')
plot(df2['s-length'], df2['p-width'], 'r+', label='Iris-versicolor')
plot(df3['s-length'], df3['p-width'], 'g+', label='Iris-virginica')
plt.legend(loc='upper left')
# plt.title("sepal length & petal width")  # petal
plt.xlabel('sepal length')
plt.ylabel('petal width')
# show()

plt.subplot(2, 2, 4)
plot(df1['p-length'], df1['p-width'], 'b+', label='Iris-setosa')
plot(df2['p-length'], df2['p-width'], 'r+', label='Iris-versicolor')
plot(df3['p-length'], df3['p-width'], 'g+', label='Iris-virginica')
plt.legend(loc='upper left')
# plt.title("petal length & petal width")  # petal
plt.xlabel('petal length')
plt.ylabel('petal width')
# show()

plt.show()

from pandas.plotting import autocorrelation_plot

auto = pandas.Series(dataSet1['s-length'])
autocorrelation_plot(auto)
plt.show()

from pandas.plotting import radviz

radviz(dataSet, 'type')
plt.show()

import seaborn as sns

sns.pairplot(dataSet, hue='type', size=3, diag_kind='kde')
plt.show()
