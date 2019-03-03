import quandl
import matplotlib.pyplot as plt
import numpy as np
msf = quandl.get('WIKI/FB', start_date="2017-01-01", end_date="2018-08-20")

plt.plot(range(0, len(msf/7)),msf)
plt.show()