import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


data = pd.read_csv('PatientData.csv', header=None)

datanp = data.to_numpy()

des = data.describe()
desnp = des.to_numpy()
#print(des)

# ts = []

for y in range(datanp.shape[0]):
	for x in range(datanp.shape[1]):
		# t = type(datanp[y][x])
		# if t not in ts:
		# 	ts.append(t)
		try:
			datanp[y][x] = float(datanp[y][x])
		except:
			datanp[y][x] = desnp[1][x]
		# if type(datanp[y][x]) is str:
		# 	# replace data with mean
		# 	print(y, x)
		# 	datanp[y][x] = desnp[1][x] #data.mean()[x]


datanp = datanp.astype(float)

cs = []

for feature in range(datanp.shape[1]):
	x = datanp[:, feature]
	y = datanp[:, -1]

	c = np.cov(x, y)
	cs.append(c[0][1])

	#plt.scatter(x, y)
	#plt.show()

cs = np.array(cs)

c2 = np.cov(datanp.transpose())
c2 = c2[:, -1]

print(np.argmax(c2))

x = datanp[:, np.argmax(c2)]
y = datanp[:, -1]
plt.scatter(x,y)
plt.show()




