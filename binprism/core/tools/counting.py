import numpy as np

def array(dist, times):
    '''
    Performs the function spectranspo.TimeDist.count_events() between all sequential pairs of times formed from an input array

    Parameters
    ----------
    dist (spectranspo.TimeDist):
        Temporal distribution of events
    times (array-like):
        Array of times

    Returns
    -------
    counts (array):
        Array of counts
    '''
    for time in times:
        if time < dist.time_range[0] or time > dist.time_range[1]:
            raise ValueError('Times must be within the time range of the distribution')

    counts = np.empty_like(times, dtype = np.float)
    N = len(times)
    for i in range(N-1):
        counts[i] = dist.count_events(times[i], times[i+1])
    counts[N-1] = dist.count_events(times[N-1], times[0] + dist.time_range[1] - dist.time_range[0])

    return counts