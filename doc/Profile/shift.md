# binprism.Profile.shift
**`Profile.shift(amount)`** <br />
Shifts a profile by the specified amount

## Parameters
**amount (numeric):** *Amount in the units specified by* `time_dist` *to shift the demand*

## Returns
**shifted_profile (binprism.Profile):** *Profile shifted by the amount specified*

## Examples
```
>>> profile0 = bp.fit([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200], range(0, 24, 2), 5, (0, 24))
>>> profile1 = profile0.shift(3)
>>> profile2 = profile0.shift(12)
>>> profile3 = profile0.shift(-2)
>>> profile0.plot(288, color = 'k', label = 'Original Profile')
>>> profile1.plot(288, color = 'r', label = 'Shifted +3 Hours')
>>> profile2.plot(288, color = 'g', label = 'Shifted +12 Hours')
>>> profile3.plot(288, color = 'b', label = 'Shifted -2 Hours')
>>> plt.xlim(profile0.time_range)
>>> plt.xticks(range(0, 25, 3))
>>> plt.xlabel('Hour')
>>> plt.ylabel('Events per Hour')
>>> plt.legend(loc = 'upper right')
>>> plt.grid(True)
>>> plt.show()
```
![alt text](ProfileShiftExample.png "Profile.shift() Example")