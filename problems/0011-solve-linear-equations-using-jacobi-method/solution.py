import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	'''
	first, we check that A is a square matrix.
	then, we also check that the row and column entries are the same for A then also compare the square matrix A with the number b.

	then we proceed to extract the diagonal from A and build a square matrix with the diagonal as diagonal entries and zeros as any other entries.

	and then finally, we proceed to run the iterations 
	'''
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)

	if A.ndim != 2  or len(A) != len(A[0]) or len(A) != len(b):
		return -1
	D = np.diag(A)
	if np.any(D==0):
		return -1

	R = A - np.diagflat(D)
	x = np.zeros_like(b)

	for _ in range(n):
		x = (b - R @ x) / D 
	
	return np.round(x, 4).tolist()