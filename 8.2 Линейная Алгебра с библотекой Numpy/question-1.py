import numpy as np

def no_numpy_scalar(v1, v2):
    scalar = 0
    for i in range(len(v1)):
        scalar += v1[i]*v2[i]
        
    result = scalar
    return result

def numpy_scalar (v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    c = np.dot(v1,v2)
    result = c
    return result
