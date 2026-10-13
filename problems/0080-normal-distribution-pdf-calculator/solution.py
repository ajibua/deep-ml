import math
import numpy as np
def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	first = np.sqrt(2*np.pi*(std_dev**2))
	second = (x - mean) ** 2
	third = 2*(std_dev**2)
	final = (1/first) * math.exp((-(second)**2)/third)
	return np.round(final, 4)