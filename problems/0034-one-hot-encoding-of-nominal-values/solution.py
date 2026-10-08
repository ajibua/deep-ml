import numpy as np

def to_categorical(x, n_col=None):
	if n_col is None:   # define n_col if it isn't given.
		n_col = np.max(x) + 1

	one_hot = np.zeros((len(x), n_col))    # creates a matrix of zeroes with one row per sample.
	one_hot[np.arange(len(x)), x] = 1   # gives both the row and column numbers.
	
	return one_hot.tolist()