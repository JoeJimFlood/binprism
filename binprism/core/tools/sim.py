import numpy as np

def place(point, ranges):
    '''
    Places a point between two points within an array

    Parameters
    ----------
    point (numeric):
        Point to place
    ranges (array):
        Array of points to place point in between

    Returns
    -------
    range_index (int):
        Index of the start of the range that the point is placed in. If no range is found, it returns nan
    '''
    for i in range(len(ranges)-1):
        if point >= ranges[i] and point <= ranges[i+1]:
            return i
    print('Range not found')
    return np.nan
place = np.vectorize(place, excluded = [1])

def get_initial_t(p, dist, n_interpolation_points):
    '''
    Computes initial time guesses for Newton-Raphson iteration by computing the value of the quantile function at evenly-spaced points and interpolating linearly

    Parameters
    ----------
    p (float or array):
        Probability value(s) to evaluate quantile function at
    dist (spectranspo.TimeDist):
        TimeDist object being used
    n_interpolation_points (int):
        Number of interpolation points to divide quantile function

    Returns
    -------
    t (float or array):
        Initial time value(s) for Newton-Raphson iteration
    '''
    t_interp = np.linspace(dist.time_range[0], dist.time_range[1], n_interpolation_points + 2)
    p_interp = dist.cdf(t_interp)

    p_range = place(p, p_interp)

    t0 = t_interp[p_range]
    t1 = t_interp[p_range + 1]
    p0 = p_interp[p_range]
    p1 = p_interp[p_range + 1]
    slope_range = (t1 - t0)/(p1 - p0)

    t = slope_range*(p - p0) + t0

    return t