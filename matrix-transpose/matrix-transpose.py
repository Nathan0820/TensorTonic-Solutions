import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows, cols = len(A), len(A[0])
    res = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(A[j][i])
        res.append(new_row)

    return np.array(res)
            
    
