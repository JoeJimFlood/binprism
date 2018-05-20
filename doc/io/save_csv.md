# binprism.save.csv
**`binprism.save.csv(fp)`** <br />
Saves profile list as a csv by first [creating a data frame](save_df.md) and then saving that data frame as a csv

## Parameters
**fp(str):** *Filepath to save profiles to*

## Example
```
>>> eb_counts = [590, 353, 301, 230, 393, 655, 1469, 2067, 2549, 2375, 1783, 2076, 
...              2193, 2017, 2513, 3262, 3294, 2915, 2657, 2412, 2323, 1928, 1925, 1118]
>>> wb_counts = [387, 316, 237, 219, 442, 1491, 2472, 2716, 2809, 2294, 2159, 1991,
...              2380, 2119, 2052, 2333, 2434, 2122, 2188, 2385, 1821, 1760, 1314, 836]
>>> hours = range(24)
>>> n_harmonics = 6
>>> time_range = (0, 24)
>>> eb_profile = bp.fit(eb_counts, hours, n_harmonics, time_range)
>>> wb_profile = bp.fit(wb_counts, hours, n_harmonics, time_range)
>>> bp.save([eb_profile, wb_profile]).csv('BinPrismCSVExample.csv')
```
[Output](BinPrismCSVExample.csv)
