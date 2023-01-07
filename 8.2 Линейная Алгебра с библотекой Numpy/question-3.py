import numpy as np

def calculate_loss_function(X, w, y):
    Xw = np.dot(X, w)
    diff = Xw - y
    norm = np.linalg.norm(diff)
    return norm ** 2
