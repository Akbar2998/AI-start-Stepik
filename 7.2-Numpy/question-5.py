import numpy as np

def cumulative_mean_2d(A):
    R = np.array(A)
    r = (np.cumsum(R[0,:]) / np.arange(1,(R[0,:]).size + 1))
    l = (np.cumsum(R[1,:]) / np.arange(1,(R[1,:]).size + 1))
    z = np.array([r,l])
    return z
