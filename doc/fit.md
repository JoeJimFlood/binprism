# binprism.fit
**`binprism.fit(data, bins, n_harmonics, time_range)`** <br />
Fits a profile to best match binned data by solving the linear system of equations described in the [methodology](methodology.md) section.

## Parameters
**data (array-like):** *Data to fit profile to match* <br />
**bins (array-like):** *Start time of each data bin. The length must be the same as* `data` <br />
**n_harmonics (int):** *Maximum number of harmonics used in fitting the log-pdf of the underlying distribution* <br />
**time_range (tuple):** *Length-2 tuple indicating the values that map to 0 and 2&#960, respectively, in the underlying distribution*

## Returns
**Profile (binprism.Profile):** *Profile fit from input data*
