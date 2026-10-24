import  numpy as np
from    tensorflow import keras
from    pathlib import Path



def prep(X, prep_info):

    """ Apply the training-set preprocessing to raw feature rows.

    - Zeros in zero-as-missing columns are replaced with training medians
    - every column is standardised with training means/std

    X: array of shape (n,8), columns in prep_data["feature_order"].
    Returns a float32 array of the same shape.
    """
    X = X.copy()

    medians = np.array(prep_info["medians"], dtype = "float32")
    mean    = np.array(prep_info["mean"], dtype = "float32")
    std     = np.array(prep_info["std"], dtype = "float32")

    # zero --> Nan
    for col_name in prep_info["zero_as_missing"]:
        col_idx = prep_info["feature_order"].index(col_name)
        X[X[:, col_idx] == 0, col_idx] = np.nan        # inside the loop: runs for every column
    
    # 2. Nan --> median
    for col_idx in range(X.shape[1]):
        missing = np.isnan(X[:, col_idx])
        X[missing, col_idx] = medians[col_idx]
    
    return ((X - mean)/ std).astype("float32")
    # print(medians)
