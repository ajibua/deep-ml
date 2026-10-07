import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	#Your code here, make sure to round
	trans_X = np.transpose(X)
	mat = trans_X @ X
	trans_inv = np.linalg.inv(mat)
	final_result = trans_inv @ trans_X @ y
	return np.round(final_result, 4).tolist()