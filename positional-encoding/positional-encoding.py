import numpy as np
import math

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len).reshape(-1, 1)

    i_sin = np.arange(math.ceil(d_model / 2)).reshape(1, -1) 
    i_cos = np.arange(d_model // 2).reshape(1, -1) 
    
    angles_sin = pos / np.power(base, 2 * i_sin / d_model)  
    angles_cos = pos / np.power(base, 2 * i_cos / d_model)

    PE = np.zeros((seq_len, d_model))

    PE[:, 0::2] = np.sin(angles_sin) 
    PE[:, 1::2] = np.cos(angles_cos)

    return PE