import numpy as np
def birthday_problem(n: int, days: int = 365) -> float:
    """
    Calculate the probability that at least two people share the same birthday.
    
    Args:
        n: Number of people in the group
        days: Number of days in a year (default 365)
    
    Returns:
        float: Probability of at least one shared birthday, rounded to 4 decimal places
    """
    if n > days:
        return 1.0
    P_no_match = 1.0
    for i in range(n):
        P_no_match *= (days - i)/days
    return np.round(1 - P_no_match,4)