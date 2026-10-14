import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    result = data.copy()
    for j in range(len(data[1])):   # we loop through the columns.
        col = data[:,j]
        mask = np.isnan(col)
        valid = col[~mask]

        if valid.size == 0:  #skip columns with nothing.
            continue

        # Define each strategy filling conditions.
        if strategy == 'mean':
            fill = np.mean(valid)
        elif strategy == 'median':
            fill = np.median(valid)
        else:
            values,count = np.unique(valid, return_counts=True)
            fill = values[np.argmax(count)]
        result[mask, j] = fill

    return result


    