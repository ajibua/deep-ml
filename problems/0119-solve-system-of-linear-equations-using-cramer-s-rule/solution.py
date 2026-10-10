import numpy as np

def cramers_rule(A, b):
    A = np.array(A)
    b = np.array(b)
    if len(A) != len(A[1]) or len(A[0]) != len(b):
        return -1
    
    det_A = np.linalg.det(A)
    if det_A == 0:
        return -1

    n = len(A[0])
    x = np.zeros(n)

    for i in range(n):
        A_i = A.copy()         
        A_i[:, i] = b          
        x[i] = np.linalg.det(A_i) / det_A

    return np.round(x, 4).tolist()