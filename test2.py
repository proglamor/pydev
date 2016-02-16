from __future__ import division
from __future__ import print_function
import numpy as np
import scipy as sp
import pandas as pd
import sklearn as sk
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
from xlwings.constants import LineStyle
sns.set()
 

plt.figure(figsize=(8, 6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
plt.xlim(-4.0, 4.0)
plt.ylim(-1.0, 1.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.figure(figsize=(8, 6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
plt.xlim(-4.0, 4.0)
plt.ylim(-1.0, 1.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))



plt.plot(X, C, color="blue", linewidth=2, LineStyle="-")
plt.plot(X, S, color="red", linewidth=5, linestyle="--")

plt.show()





