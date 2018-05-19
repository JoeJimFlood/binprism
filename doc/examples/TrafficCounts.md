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
>>> n_harmonics = 4
>>> time_range = (0, 24)
>>> eb_profile = bp.fit(eb_counts, hours, n_harmonics, time_range)
>>> wb_profile = bp.fit(wb_counts, hours, n_harmonics, time_range)
>>> plt.bar(hours, eb_counts, 24*[1], align = 'edge', alpha = 0.5,
...         facecolor = '#8080ff', edgecolor = 'k', label = 'Eastbound Counts')
>>> plt.bar(hours, wb_counts, 24*[1], align = 'edge', alpha = 0.5,
...         facecolor = '#ff8080', edgecolor = 'k', label = 'Westbound Counts')
>>> eb_profile.plot(288, color = 'b', linewidth = 2, label = 'Eastbound Profile')
>>> wb_profile.plot(288, color = 'r', linewidth = 2, label = 'Westbound Profile')
>>> plt.xlim(0, 24)
>>> plt.ylabel('Vehicles per Hour')
>>> plt.xticks(list(range(0, 25, 3)), ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM'])
>>> plt.legend(loc = 'best')
>>> plt.show()
```
![alt text](TrafficCounts.png "Fitting profiles to match hourly traffic counts") </br>
Now estimate 15-minute counts between 5 and 10 AM.
```
>>> import pandas as pd
>>> from datetime import datetime, timedelta
>>> times = []
>>> start_time = datetime(1, 1, 1, 5)
>>> for i in range(20):
...     times.append(start_time.strftime('%H:%M'))
...     start_time += timedelta(minutes = 15)
>>> eb_15min_counts = eb_profile[5:10:0.25]
>>> wb_15min_counts = wb_profile[5:10:0.25]
>>> counts_15min = pd.DataFrame({'Start Time': times, 'Eastbound': eb_15min_counts, 'Westbound': wb_15min_counts})
>>> counts_15min = counts_15min.set_index('Start Time')
>>> counts_15min
             Eastbound   Westbound
Start Time                        
05:00       131.980478  220.020586
05:15       157.476864  279.719953
05:30       189.112545  351.197888
05:45       227.384562  432.166668
06:00       272.285914  517.933100
06:15       323.050427  601.698326
06:30       377.963770  675.678870
06:45       434.341025  732.812569
07:00       488.751058  768.452534
07:15       537.495831  781.383193
07:30       577.249089  773.798306
07:45       605.674481  750.367531
08:00       621.830784  716.873672
08:15       626.246603  678.950663
08:30       620.671278  641.250753
08:45       607.617211  607.102892
09:00       589.852662  578.541905
09:15       569.978038  556.531083
09:30       550.153844  541.231644
09:45       531.983684  532.235317
```
Finally, simulate a day of Eastbound counts.
```
>>> sim_trips = eb_profile.sim(int(eb_profile.total))
>>> sim_trips[:12]
array([ 10.28490207,  17.01079742,   9.68251655,  13.9904729 ,
        12.45575775,   8.95413898,  14.45038468,  19.00851263,
        17.89740555,  18.1722341 ,  13.60739526,  18.57917681])
>>> plt.hist(sim_trips, 24, facecolor = 'b', edgecolor = 'k')
>>> plt.xlim(0, 24)
>>> plt.xticks(list(range(0, 25, 3)), ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM'])
>>> plt.ylabel('Number of Simulated Trips')
>>> plt.show()
```
![alt text](TrafficCountsSim.png "Simulated houly counts") </br>
Compare with observed counts.
```
>>> from scipy.stats import pearsonr
>>> sim_counts = np.histogram(sim_trips, 24)[0]
>>> (r, p) = pearsonr(sim_counts, eb_counts)
>>> plot_range = (0, 1.1*max(max(eb_counts), max(sim_counts)))
>>> plt.scatter(sim_counts, eb_counts, color = 'b', alpha = 0.7)
>>> plt.plot(plot_range, plot_range, color = 'k', linestyle = ':')
>>> plt.xlabel('Simulated Counts')
>>> plt.ylabel('Observed Counts')
>>> plt.xlim(plot_range)
>>> plt.ylim(plot_range)
>>> plt.grid(True)
>>> plt.title('Observed Counts vs. Simulated Counts \nr={}'.format(round(r, 3)))
>>> plt.show()
```
![alt text](TrafficCountCompare.png "Comparison of simulated and observed counts")
