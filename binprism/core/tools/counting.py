import numpy as np

def array(profile, times):
    '''
    Performs the function binprism.Profile.count_events() between all sequential pairs of times formed from an input array

    Parameters
    ----------
    profile (binprism.Profile):
        Temporal distribution of events
    times (array-like):
        Array of times

    Returns
    -------
    counts (array):
        Array of counts
    '''
    counts = np.empty_like(times, dtype = float)[:-1]
    N = len(times)
    for i in range(N-1):
        counts[i] = profile.count_events(times[i], times[i+1])

    return counts