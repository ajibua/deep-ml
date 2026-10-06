import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]] | int:
	if len(T) != len(T[0]) or len(S) != len(S[0]):
		return -1
	if abs(np.linalg.det(T)) < 1e-10 or abs(np.linalg.det(S)) < 1e-10:
		return -1
	if len(A) != len(T) or len(A[0]) != len(S):
		return -1

	T_inv = np.linalg.inv(T)
	result = T_inv @ A @ S
	return np.round(result, 3).tolist()