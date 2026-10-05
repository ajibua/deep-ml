import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eig = np.linalg.eigvals(matrix)
	sorted_eig = sorted(eig, reverse=True)
	return sorted_eig