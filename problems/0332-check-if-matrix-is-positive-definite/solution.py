import numpy as np

def check_positive_definite(matrix: list) -> dict:
    """
    Check if a matrix is positive definite and compute its eigenvalues.
    
    Args:
        matrix: A 2D list representing a square matrix
        
    Returns:
        dict with 'is_positive_definite' (bool) and 'eigenvalues' (list of floats sorted ascending)
    """
    eig_vals = np.linalg.eigvals(matrix) 
    eig_vals = np.sort(eig_vals.real)
    return{"is_positive_definite":bool(np.all(eig_vals>0)), "eigenvalues":np.round(eig_vals, 4).tolist()}