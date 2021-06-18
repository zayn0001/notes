import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

h=1 #mean
sd=1 #sd
n=50  #num of points

def gen_data(n,h,sd1,sd2):
    x1 = ss.norm.rvs(-h,sd1,n)
    y1 = ss.norm.rvs(0,sd1,n)
    x2 = ss.norm.rvs(h,sd2,n)
    y2 = ss.norm.rvs(0,sd2,n)
    return (x1,y1,x2,y2)

def plot_data(x1,y1,x2,y2):
    plt.figure()
    plt.plot(x1,y1,'o',ms=2,label='1')
    plt.plot(x2,y2,'o',ms=2,label='2')
    plt.xlabel('$X$')
    plt.ylabel('$Y$')
    plt.legend(loc='lower right')


n = 1000
m = 1.5
sd1=1
sd2=1.5
(x1,y1,x2,y2) = gen_data(n,m,sd1,sd2)
plot_data(x1, y1, x2, y2)

#logistic regression = linear model that models probabilities
#log(p(x)/1-p(x)) = B_0 + B_1 * X_! +....

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

X = np.vstack((np.vstack((x1, y1)).T , np.vstack((x2, y2)).T))
y = np.hstack((np.repeat(1,n),np.repeat(2,n)))

#creates a sets of data that can be used for training and 
#testing your data when you dont have a seperate dataset to train it
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5,random_state=1)
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
clf.predict_proba(np.array([-2,0]).reshape(1,-1))
clf.predict(np.array([-2,0]).reshape(1,-1))

plt.figure()
plt.plot(X_train[:,0][y_train==1],X_train[:,1][y_train==1],'o', ms=2, label='1')
plt.plot(X_train[:,0][y_train==2],X_train[:,1][y_train==2],'o', ms=2,label='2')
plt.legend(loc='lower right')


def plot_probs(ax, clf, class_no):
    xx1, xx2 = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1))
    probs = clf.predict_proba(np.stack((xx1.ravel(), xx2.ravel()), axis=1))
    Z = probs[:,class_no]
    Z = Z.reshape(xx1.shape)
    CS = ax.contourf(xx1, xx2, Z)     #plotting
    cbar = plt.colorbar(CS)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
    
plt.figure()
ax = plt.subplot(211)
plot_probs(ax,clf,0)
plt.title('Pred. prob for class 1')
ax = plt.subplot(212)
plot_probs(ax,clf,1)
plt.title('Pred. prob for class 2')


#meshgrid gives two matrices corresponding to the different axes
#in xx1 each row contains all the possible values on the x-axis (-5,-4.9,...5)
#there are as many number of rows as there are points on the y axis which in this case is the same
#in xx2 each row contains a single probable value on y-axis for each x-axis value
#as many times as there are values on the x-axis(-5,-5,-5,-5....-5) for first row
# as in the x axis because it is a square (-5 to 5)
