import numpy as np
def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    count_x = 0
    count_x_and_y = 0
    for xi, yi in data:
      if xi==x:
        count_x +=1
        if yi==y:
          count_x_and_y += 1
    
    if count_x == 0:
      return 0.0

    final = count_x_and_y/count_x
    return np.round(final, 4)