# binprism.Profile.time2angle
**`Profile.time2angle(t)`** <br />
Converts a time in the profile's units to angle between zero and 2-pi

## Parameters
**t (numeric or array-like):** *Time(s) to convert to angles*

## Returns
**theta (numeric or array-like):** *Angle(s) that have been converted*

## Examples
```
>>> profile1 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile1.time2angle(np.array([0, 6, 12, 18, 24]))/np.pi
array([ 0. ,  0.5,  1. ,  1.5,  2. ])
>>> profile2 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 12, 1), 5, (0, 12))
>>> profile2.time2angle(np.array([0, 3, 6, 9, 12]))/np.pi
array([ 0. ,  0.5,  1. ,  1.5,  2. ])
```
