import matplotlib.pyplot as plt
import random
import numpy as np
rolls = []
for k in range(10000):
	rolls.append(random.choice(range(1,7)))
#plt.hist(rolls, bins=np.linspace(0.5,6.5,7))
#plt.show()
#help(plt.hist)


ys = []
for rep in range(100):
	y = 0
	for k in range(10):
		y = y + random.choice(range(1,7))
	ys.append(y)

#plt.hist(ys, bins=np.linspace(9.5,60.5,62))
#plt.show()

array = np.random.random(5)
matrix = np.random.random((5,3))
#print(array)
x = np.random.normal(0,1, (3,2))       
#mean, SD, no of outcomes/dimension
#print(x)

x = np.random.randint(1,7, (1000,100))
#print(x)
y = np.sum(x, axis=1)
#axis = 0 : rows
#axis = 1: columns
#print(y)
#plt.hist(y, bins=np.linspace(100,600,502))
#plt.show()

import time
start = time.time()

end = time.time()
#print(end-start)

deltaxs = np.random.normal(0,1,(2,5))
#print(deltaxs)
disp = np.cumsum(deltaxs, axis=1)
#np.cumsum takes an array of the cumulatives
#if columns are selected, the 1st column is added to the second and so on
origin = np.array([[0],[0]])
disp = np.concatenate((origin, disp), axis=1)
print(disp)
plt.plot(disp[0], disp[1], 'go-')
plt.show()

#np.concatenate take an iterable of arrays to be concatenated and then binds them along the axis mentioned
