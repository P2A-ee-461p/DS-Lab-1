from random import random
import math

import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline



def genX():
	if random()<0.5:
		return -1
	else:
		return 1

def genZn(n):
	ans = 0
	for _ in range(n):
		ans += genX()
	ans = ans / math.sqrt(n)
	return ans

samples10 = [genZn(10) for i in range(1000)]
samples50 = [genZn(50) for i in range(1000)]
samples250 = [genZn(250) for i in range(1000)]


#print(genX())
#print(genZn(5))

#x = np.random.normal(size = 1000)

plt.subplot(1, 3, 1)
plt.hist(samples10, density=True, bins=30)
plt.title('1000 samples of Z_10')
plt.xlabel('Zn value')
plt.ylabel('Frequency')


plt.subplot(1, 3, 2)
plt.hist(samples50, density=True, bins=30)
plt.title('1000 samples of Z_50')
plt.xlabel('Zn value')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(samples250, density=True, bins=30)
plt.title('1000 samples of Z_250')
plt.xlabel('Zn value')
plt.ylabel('Frequency')

plt.show()