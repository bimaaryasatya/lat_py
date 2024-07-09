import numpy as np

def avgr(arr):
    return np.mean(arr)

def ab_avg(arr):
    return sum(arr > avgr(arr))
    #return sum(True for i in arr if i > avgr(arr))

def max_nilai(arr):
    return np.max(arr)

def min_nilai(arr):
    return np.min(arr)

