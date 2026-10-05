import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	sca_mul = np.dot(matrix, scalar)
	return sca_mul.tolist()