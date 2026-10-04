import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		return np.mean(matrix, axis=1).tolist()
	else:
		return np.mean(matrix, axis=0).tolist()