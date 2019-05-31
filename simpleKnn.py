import numpy as np
import matplotlib.pyplot as plt

# find the closest dot to the testDot (pythagorean theorum) and return the distance
def minDistance(dots, dot):
    dist = (dots - dot) ** 2
    #print 'dist 1:', dist
    dist = np.sum(dist, axis=1) # axis=1 sums the columns
    #dist = np.sum(dist, axis=0) # axis=0 sums the rows
    #print 'dist 2:', dist
    dist = np.sqrt(dist)
    #print 'dist 3:', dist
    min = np.amin(dist) # find the minimum
    return min

# create two sets of dots and a random dot
greenDots = np.random.uniform(low=0, high=1, size=(50, 2))
blueDots = np.random.uniform(low=1, high=2, size=(50, 2))
redDot = np.random.uniform(low=0, high=2, size=(1, 2))

# compare redDot to see what group it is part of
greenMin = minDistance(greenDots, redDot)
blueMin = minDistance(blueDots, redDot)
if greenMin <= blueMin:
    print 'redDot is part of the green group'
else:
    print 'redDot is part of the blue group'

plt.scatter(greenDots[:,0], greenDots[:,1], color='green')
plt.scatter(blueDots[:,0], blueDots[:,1], color='blue')
plt.scatter(redDot[:,0], redDot[:,1], color='red')
plt.show()

