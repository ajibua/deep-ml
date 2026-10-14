import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	outlier_indices = []
	cleaned_data = []
	Q_1 =np.percentile(data, 25)
	Q_3 = np.percentile(data, 75)

	IQR = Q_3 - Q_1

	upper_bound = Q_3 + k * IQR
	lower_bound = Q_1 - k * IQR
	for i,v in enumerate(data):
		if v > upper_bound  or v < lower_bound:
			outlier_indices.append(i)
		else:
			cleaned_data.append(v)
	return {
		'cleaned_data': cleaned_data,
		'outlier_indices':outlier_indices,
		'upper_bound':upper_bound,
		'lower_bound':lower_bound
	}