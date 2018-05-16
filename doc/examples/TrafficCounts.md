# Traffic Counts
Traffic counts available from the [Delaware Valley Regional Planning Commission](https://www.dvrpc.org/webmaps/TrafficCounts/). </br>
</br>
The following were the hourly traffic volumes on the Benjamin Franklin Bridge between Philadelphia, Pennsylvania and Camden, New Jersey on Thursday, March 12, 2015:

|Hour     |Eastbound Counts|Westbound Counts
|---------|---------------:|---------------:|
|12AM-1AM |590             |387             |
|1AM-2AM  |353             |316             |
|2AM-3AM  |301             |237             |
|3AM-4AM  |230             |219             |
|4AM-5AM  |393             |442             |
|5AM-6AM  |655             |1491            |
|6AM-7AM  |1469            |2472            |
|7AM-8AM  |2067            |2716            |
|8AM-9AM  |2549            |2809            |
|9AM-10AM |2375            |2294            |
|10AM-11AM|1783            |2159            |
|11AM-12PM|2076            |1991            |
|12PM-1PM |2193            |2380            |
|1PM-2PM  |2017            |2119            |
|2PM-3PM  |2513            |2052            |
|3PM-4PM  |3262            |2333            |
|4PM-5PM  |3294            |2434            |
|5PM-6PM  |2915            |2122            |
|6PM-7PM  |2657            |2188            |
|7PM-8PM  |2412            |2385            |
|8PM-9PM  |2323            |1821            |
|9PM-10PM |1928            |1760            |
|10PM-11PM|1925            |1314            |
|11PM-12PM|1118            |836             |

The following code fits profiles to match the data:
```
>>> eb_counts = [590, 353, 301, 230, 393, 655, 1469, 2067, 2549, 2375, 1783, 2076, 
...              2193, 2017, 2513, 3262, 3294, 2915, 2657, 2412, 2323, 1928, 1925, 1118]
>>> wb_counts = [387, 316, 237, 219, 442, 1491, 2472, 2716, 2809, 2294, 2159, 1991,
...              2380, 2119, 2052, 2333, 2434, 2122, 2188, 2385, 1821, 1760, 1314, 836]
>>> hours = list(range(24))
>>> n_harmonics = 5
>>> time_range = (0, 24)
>>> eb_profile = bp.fit(eb_counts, hours, n_harmonics, time_range)
>>> wb_profile = bp.fit(wb_counts, hours, n_harmonics, time_range)
>>> plt.bar(hours, eb_counts, 24*[1], align = 'edge', fill = False, edgecolor = 'b', label = 'Eastbound Counts')
>>> plt.bar(hours, wb_counts, 24*[1], align = 'edge', fill = False, edgecolor = 'r', label = 'Westbound Counts')
>>> plt.xlim(0, 24)
>>> plt.ylabel('Vehicles per Hour')
>>> plt.xticks(list(range(0, 25, 3)), ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM'])
>>> plt.show()
```
