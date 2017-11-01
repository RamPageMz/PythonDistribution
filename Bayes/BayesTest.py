# Python file
# Name  :   BayesTest
# Create:   2017/10/25 15:46
# Author:   Ma
# Contact   1033516561@qq.com

# Quote:    https://zhuanlan.zhihu.com/p/27012448?utm_source=tuicool&utm_medium=referral

# Question:
# 假设有两碗曲奇饼，碗A包含30个香草曲奇饼和10个巧克力曲奇饼，碗B这两种曲奇饼各20个。 现在假设你在不看的情况下随机地挑一个碗拿一块饼，得到了一块香草曲奇饼。
# 问题：从碗A渠道香草曲奇饼的概率是多少

class Bayes(object):
    # 定义Bayes类，初始化创建一个dict类型的容器container。该容器是为了储存贝叶斯各项信息。key键存储假设，value值存储概率
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


# 实例化Bayes类
bayes = Bayes()

# 先验概率
bayes.set('Bow_A', 0.5)  # P(碗A)=1/2
bayes.set('Bow_B', 0.5)  # P(碗B)=1/2

# 后验概率
bayes.mult('Bow_A', 0.75)  # P(香草饼|碗A)=3/4
bayes.mult('Bow_B', 0.5)  # P(香草饼|碗B)=1/2

bayes.normalize()
prob = bayes.prob('Bow_A')  # P(碗A|香草饼)
print('从碗A渠道香草曲奇饼的概率:{}'.format(prob))
