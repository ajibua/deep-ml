import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	C_inv = np.linalg.inv(C)
	matr_mul = C_inv @ B
	return np.round(matr_mul, 4).tolist()