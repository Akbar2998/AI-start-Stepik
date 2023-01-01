import numpy as np
def no_numpy_mult(first, second):
    c = [[0 for _ in range(len(first))] for _ in range(len(first))]
    for i in range(len(first)):
        for j in range(len(first)):
            for k in range(len(first)):
                c[i][j] += first[i][k]*second[k][j] 
    result = c
    return result

def numpy_mult(first, second):
    result = first @ second
    return result
