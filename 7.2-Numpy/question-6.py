import numpy as np

def transform(X):
    R = np.array(X)
    R[::2] = R[::2]**3
    R[1::2] = 1
    return R
