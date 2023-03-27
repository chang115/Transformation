import numpy as np
from hwk07_p3_soln import project, rotate, moveTo

# NOTE: you do NOT need to rewrite the `project`, `rotate`, or `moveTo` functions 
# as they are imported above

def ballTransform4(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    org = moveTo(loc, np.array([0.0, 0.0, 0.0, 0.0]))
    rad = 2.0 * np.pi * (i/150.0)
    rot = rotate(0, 0, -rad)
    roll = rot @ org
    back = moveTo(np.array([0.0, 0.0, 0.0, 0.0]), np.array([(loc[0] + 20 * i/150), loc[1] + 0, loc[2] + 0, loc[3] + 0]))
    P = project(100)
    return P @ back @ roll
