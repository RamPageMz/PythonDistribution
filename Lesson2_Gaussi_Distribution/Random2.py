# Python file
# Name  :   Random2
# Create:   2017/10/25 17:13
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin
from scipy import stats
from scipy.stats import norm

import numpy as np
import pylab as pl


mu = 0  # mean
sigma = 2  # standard deviation
x = np.arange(-10, 10, 0.1)
y = stats.norm.pdf(x, mu, sigma)
print(y)
pl.plot(x, y)
pl.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu, sigma))
pl.xlabel('x')
pl.ylabel('Probability density', fontsize=15)
pl.show()
