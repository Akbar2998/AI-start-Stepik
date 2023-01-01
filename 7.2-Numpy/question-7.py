import numpy as np

def diag_2k(a):
    summa = 0
    for i in range(0,a.shape[1]):
        if a[i,i] % 2 == 0:
            summa += a[i,i]
    return summa
