# binprism.Profile.eval
**`Profile.eval(t)`** <br />
Evaluates the profile at time `t`

## Parmeters
**t (numeric or array-like):** *Time(s) at which to evaluate the event rate in the units specified by* `time_range`

## Returns
**event_rate (numeric or array-like):** *Event rate evaluated at time* `t`

## Example
```
>>> profile = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile.eval(np.array([0, 6, 12, 18, 24]))
array([  56.79744691,  124.0332684 ,   32.45300343,   64.20548254,
         56.79744691])
```
