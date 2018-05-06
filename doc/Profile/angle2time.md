# binprism.Profile.angle2time
**`Profile.angle2time(theta)`** <br />
Converts angle between zero and 2-pi to time in units specified by `time_range`

## Parameters
**theta (numeric or array-like):** *Angle(s) to convert to time*

## Returns
**t (float or array-like):** *Time(s) that have been converted*

## Examples
```
>>> profile1 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile2 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 12, 1), 5, (0, 12))
>>> profile1.angle2time(np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]))
array([  0.,   6.,  12.,  18.,  24.])
>>> profile2.angle2time(np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]))
array([  0.,   3.,   6.,   9.,  12.])
```
