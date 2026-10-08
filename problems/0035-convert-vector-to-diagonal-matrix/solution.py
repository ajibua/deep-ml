import numpy as np

def make_diagonal(x):
	diag = np.diag(x)
	return np.round(diag, 4).tolist()