import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	dot_prd = np.dot(v1, v2)
	dot_norm = np.linalg.norm(v1) * np.linalg.norm(v2)

	if dot_norm == 0:
		return 0.0

	return dot_prd / dot_norm
