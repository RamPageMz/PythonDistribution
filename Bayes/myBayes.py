# Python file
# Name  :   myBayes
# Create:   2017/10/25 16:20
# Author:   Ma
# Contact   1033516561@qq.com


# P(H|D)=P(H)P(D|H)/P(D)
# 在考虑H和D的情况下，每项意义如下：
# P(H)称为先验概率，即在得到新数据前某一假设的概率。如没有得到掷硬币结果前，我们先假设正反面概率各位50%。
# P(H|D)称为后验概率，即看到新数据后，我们要计算的该假设的概率。
# P(D|H)是该假设下得到这一数据的概率，称为似然度。
# P(D)是任何假设下得到这一数据的概率，称为标准化常量。

class Bayes:
    def __init__(self):
        self._container = dict()

    # 输入事件的先验概率
    # name：事件名称     data：概率值
    def first(self, name, data):
        self._container[name] = data

    # 根据抽样结果 调整后验概率
    # name:事件名称     data1:似然度1     data2:似然度2
    def back(self, name1, data1, name2, data2):
        # 全概率 all
        all = data1 * self._container[name1] + data2 * self._container[name2]
        print("全概率：%.3f" % (all))
        # 计算后验概率
        back1 = data1 * self._container[name1] / all
        back2 = data2 * self._container[name2] / all
        print("后验概率：%.3f %.3f" % (back1, back2))
        # 更新概率
        self._container[name1] = back1
        self._container[name2] = back2

    # Normalize方法：归一化
    def normalize(self):
        count = 0
        for i in self._container.values():
            count = count + i
        for i, prob in self._container.items():
            self._container[i] = self._container[i] / count

    # 根据事件名 返回概率
    def show(self, name):
        return self._container[name]


bayes = Bayes()

bayes.first("method1", 0.4)
bayes.first("method2", 0.6)

# 处理5个邮件，全部正确
bayes.back("method1", 0.9 ** 5, "method2", 0.7 ** 5)
print("一次抽样后 可信度调整为：%.4f %.4f" % (bayes.show("method1"), bayes.show("method2")))

# 处理10个邮件，9个正确
bayes.back("method1", 10 * (0.9 ** 9) * (1 - 0.9), "method2", 10 * (0.7 ** 9) * (1 - 0.7))

print("一次抽样后 可信度调整为：%.4f %.4f" % (bayes.show("method1"), bayes.show("method2")))
