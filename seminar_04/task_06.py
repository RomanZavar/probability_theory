


import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

plt.hist(x, bins=15)
plt.show()

plt.boxplot(x)
plt.show()