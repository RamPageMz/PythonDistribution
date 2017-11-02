# Python file
# Name  :   Random
# Create:   2017/10/25 17:05
# Author:   Ma
# Contact   1033516561@qq.com

# Quote     http://blog.sina.com.cn/s/blog_bc2455080101ajvl.html

from scipy import stats
from scipy.stats import norm

import numpy as np
import pylab as pl

x = norm()
y = norm(loc=1.0, scale=2.0)
t = np.arange(-10, 10, 0.1)

pl.plot(t, x.pdf(t), label="$x$", color="red")
pl.plot(t, y.pdf(t), "b--", label="$y$")
pl.legend()

pl.show()
