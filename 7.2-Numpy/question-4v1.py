import numpy as np

def cumulative_mean(X):
    s = []
    for i in range(1,len(X)+1):
        l = 0
        count = 0
        for j in range(i):
            l += X[j]
            count += 1

        s.append(l/count)   

    result = s
    return result
