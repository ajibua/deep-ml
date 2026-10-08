import numpy as np

def calculate_correlation_matrix(X, Y=None):
	if Y is None: #if Y isn't given, replace it with X
		Y = X
	else:
		Y = np.asarray(Y, dtype=float)

	p = len(X[1]) #the columns in X
	full = np.corrcoef(X, Y, rowvar=False)
	corr_mat = full[:p, p:] #the correlation matrix itself.
	return np.round(corr_mat, 6).tolist() #and then the result.