# Load libraries

import pandas
import matplotlib.pyplot as plt
import statistics
import numpy as np
from pandas.plotting import scatter_matrix
from pandas.plotting import parallel_coordinates
from pandas.plotting import radviz
from scipy.stats import norm

# load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

'''
实验一：学习使用Python的第三方图形库matplotlib以及Pandas的绘图方法，样本的图形显示以及正态分布的绘制函数
自由选择样本集（注意样本数据尽可能充分）
编写python程序，实现数据集特征图形化分析
'''


def mynormal(sl, name):
    samples = []
    for i in range(0, 5000):
        j = sl.sample(frac=0.3, replace=False).mean()
        samples.append(j)
    mu = statistics.mean(samples)
    sigma = statistics.stdev(samples)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma)
    y = norm.pdf(x, mu, sigma)
    plt.plot(x, y, color='red')
    plt.title('Normal Distribution of %s sepal-length : $\mu$=%.1f, $\sigma$=%.1f' % (name, mu, sigma))
    plt.xlabel('length')
    plt.ylabel('Probability density')
    plt.show()


# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# box and whisker plots
boxcolor = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
dataset.plot(kind='box', color=boxcolor, subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist(grid=False, color='olivedrab')
plt.show()

# normal distribution
sl = dataset['sepal-length']
mynormal(sl, ' ')

# interactions between the variables
# scatter plot matrix
scatter_matrix(dataset, alpha=0.2, figsize=(6, 6), diagonal='kde', color='darkorange')
plt.show()

# parallel coordinates
plt.figure()
parallel_coordinates(dataset, 'class')
plt.show()

# RadViz
radviz(dataset, 'class')
