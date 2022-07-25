import math
import numpy as np

X = [4,5,12,7,8,9,15,17,11,22,32,3,10,15]

def mean(X):
    sum = 0
    for x in X:
        sum += x
    return sum/len(X)

print(mean(X))
print(np.mean(X))
print()

def variance(X):
    return mean([x ** 2 for x in X]) - mean(X) ** 2

print(variance(X))
print(np.var(X))
print()


def covariance(X,Y):
    if len(X) != len(Y):
        return False
    return mean([X[i] * Y[i] for i in range(len(X))]) - (mean(X) * mean(Y))

def covariance2(X,Y):
    if len(X) != len(Y):
        return False
    cov = 0
    muX, muY = mean(X), mean(Y)
    for i in range(len(X)):
        cov += (X[i] - muX) * (Y[i] - muY)
    return cov/(len(X)-1)

Y = [88,34,25,46,78,12,93,34,25,75,64,12,29,30]
print(covariance(X,Y))
print(covariance2(X,Y))
print(np.cov(X,Y)[0][1])
print()

def correlation(X,Y):
    if len(X) != len(Y):
        return False
    return covariance(X, Y)/math.sqrt(variance(X) * variance(Y))

print(correlation(X,Y))
print(np.corrcoef(X,Y)[0][1])
print()
print(correlation([102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14],[88,34,25,46,78,12,93,34,25,75,64,12,29,30,22,13,26]))
print(np.corrcoef([102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14],[88,34,25,46,78,12,93,34,25,75,64,12,29,30,22,13,26])[0][1])
print()
print(correlation([102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14],[102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14]))
print(np.corrcoef([102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14],[102,12,45,165,23,78,59,456,61,23,41,78,89,102,103,65,14])[0][1])