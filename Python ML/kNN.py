#kNN
#k nearest neighbors

#assigning a point to a category based on the categories of its neihboring points
import numpy as np
import random
from collections import Counter
p1 = np.array([1,1])
p2 = np.array([1,4])

def dist(p1,p2):
	return np.sqrt(np.sum(np.power(p2-p1,2)))
distance = dist(p1,p2)
#print(distance)

total = [1, 2, 3, 4, 2, 3, 4, 2, 1, 2, 3, 4, 2, 1, 3, 3]

def find_mode(votes):
    winners = []
    freq_list = Counter(votes)
    largest_freq = max(freq_list.values())
    for vote, freq in freq_list.items():
        if freq == largest_freq:
            winners.append(vote)
    #print(winners)
    #print(freq_list)        
    return random.choice(winners)
#print(find_mode(total))
import scipy.stats as ss
(mode, count) = ss.mstats.mode(total)
#print(mode[0])

points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])

import matplotlib.pyplot as plt
plt.plot(points[:,0],points[:,1], 'ro')
plt.plot(p[0],p[1],'bo')
plt.show()
print([points.shape])
print(np.zeros((5,2)))
print(np.zeros(5))
print(points)
print(points[0])

def find_nn(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = dist(p , points[i])
        ind = distances.argsort()
    distances = distances[ind]
    return ind[:k]

#print(find_nn(p, points, 6))

def knn_predict(p, points, categories, k=5):
    ind = find_nn(p, points, k)
    return find_mode(categories[ind])

categories = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
#print(knn_predict(p, points, categories, 2))    

def create_sd(n=50):
    '''
    Syntheti Data
    Create two sets of points from bivariate normal distribution
    '''
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    return (points, outcomes)

#points , outcomes = create_sd(20)
#n = 20
#plt.plot(points[:n,0], points[:n,1], 'bo')
#plt.plot(points[n:,0], points[n:,1], 'ro')

def make_pg(predictors, outcomes, limits, h, k):
    '''
    prediction grid
    '''
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs,ys)
    
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    return (xx,yy,prediction_grid)


def plot_prediction_grid (xx, yy, prediction_grid):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))

predictors , outcomes = create_sd()
k=50
limits = (5, 4, -3, 4)
h=0.1
(xx,yy,prediction_grid) =  make_pg(predictors, outcomes, limits, h, k)  
plot_prediction_grid(xx, yy, prediction_grid)





































