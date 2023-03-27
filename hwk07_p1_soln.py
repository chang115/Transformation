import numpy as np

def project(d):
    """
    returns the projection matrix corresponding to having the 
    viewpoint at (0, 0, d)
    and the viewing plane at z = 0 (the xy plane).
    """
    P = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, -1/d, 1]])
    return P

def houseTransform1(i, loc):
    """
    Returns the appropriate transformation matrix for the house, 
    which in this case is simply the projection matrix at d=100.
    """
    x = project(100)
    return x

def ballTransform1(i, loc):
    """
    Returns the appropriate transformation matrix for the ball,
    which in this case is simply the projection matrix at d=100.
    """
    y = project(100)
    return y




