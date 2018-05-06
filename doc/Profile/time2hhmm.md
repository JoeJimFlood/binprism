# binprism.Profile.time2hhmm
**`Profile.time2hhmm(t, format24 = None)`** <br />
Converts a time value to a time in hh:mm format.

## Parameters
**t (numeric):** *Time to display* <br />
**format24 (bool):** *Indicates whether or not to use 24-hour time format. If not specified, inferred based on local time zone.*

## Returns
**outtime (str):** *Time in hh:mm format*

## Examples
```
>>> profile1 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile2 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 12, 1), 5, (0, 12))
>>> profile1.time2hhmm(9)
'9:00 AM'
>>> profile2.time2hhmm(9)
'6:00 PM'
```
