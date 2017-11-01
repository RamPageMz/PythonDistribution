# http://python.jobbole.com/81321/

import numpy as np
import statsmodels
from scipy import stats
import pylab as pl

n = 10
p = 0.3
k = np.arange(0, 21)
binomial = stats.binom.pmf(k, n, p)

pl.plot(k, binomial, 'o-')
pl.title('Binomial: n=%i , p=%.2f' % (n, p))
