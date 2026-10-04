import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	try:
		new_shape = np.reshape(a, new_shape).tolist()
		return new_shape
	except:
		return []
	
