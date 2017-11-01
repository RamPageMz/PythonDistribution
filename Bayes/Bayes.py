# Python file
# Name  :   Bayes
# Create:   2017/10/25 16:00
# Author:   Ma
# Contact   1033516561@qq.com

# Part 1  实现例1-2的贝叶斯概率计算过程
#    假设进行n次试验，计算最后得到的
#    样本数据集文件提供每次试生产的观测值
#    程序提供界面输入先验分布值、边缘分布值，从样本文件中读出实验数据，计算后显示结果
# From ppt Lesson 1

# Question
# 实施效果的两种估计:
# 意见1：引进后, 分类准确性提高到90%
# 意见2：引进后, 分类准确性提高到70%
# 经理根据以往两部门建议情况认为：
# 意见1的可信度为40%
# 意见2的可信度为60%
# 小规模试用2次
# 处理5个邮件，全部正确
# 处理10个邮件，9个正确
# 意见1、2的可信度？


# 定义Bayes类
class Bayes(object):
    # 初始化创建一个dict类型的容器container。该容器是为了储存贝叶斯各项信息。key键存储假设，value值存储概率
    def __init__(self):
        self._container = dict()

    # Set方法是给容器添加先验假设及先验概率
    def set(self, hypothis, prob):
        self._container[hypothis] = prob

    # Mult方法：根据key查找到先验概率，并更新概率
    def mult(self, hypothis, prob):
        old_prob = self._container[hypothis]
        self._container[hypothis] = old_prob * prob

    # Normalize方法：归一化
    def normalize(self):
        count = 0
        for hypothis in self._container.values():
            count = count + hypothis
        for hypothis, prob in self._container.items():
            self._container[hypothis] = self._container[hypothis] / count

    # Prob方法：返回某一事件的概率
    def prob(self, hypothis):
        prob = self._container[hypothis]
        return prob


bayes = Bayes()

# 先验概率
bayes.set("method_A", 0.4)
bayes.set("method_B", 0.6)

# 根据抽样结果更新后验概率
