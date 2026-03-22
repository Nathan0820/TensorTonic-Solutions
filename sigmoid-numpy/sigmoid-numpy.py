import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_as_np = np.asarray(x, dtype=float)
    expo = np.exp(-x_as_np)
    return 1 / (1 + expo)
