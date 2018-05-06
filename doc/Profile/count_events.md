# binprism.Profile.count_events
**`Profile.count_events(a, b)`**
Counts the number of events between times `a` and `b`. Also works by calling `Profile[a:b]`

## Parameters
**a (numeric or array-like):** *Time(s) at which to start counting events* <br />
**b (numeric or array-like):** *Time(s) at which to end counting events* <br />

## Returns
**n_events (numeric or array_like):** *Number of events between* `a` *and* `b`

## Example
```
>>> profile = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile.count_events(12, 16)
99.50481232290764
>>> profile[12:16]
99.50481232290764
```
