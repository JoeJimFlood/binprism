# binprism.Profile
**`binprism.Profile(dist, total, time_range)`** <br />
**dist (binprism.PPD):** *Probability distribution that events follow* <br />
**total (numeric):** *Total number of events* <br />
**time_range (tuple):** *Length-2 tuple indicating the start and end times of one period of events* <br />
A profile of events distributed throughout a time period, such as events throughout the day or year.

## Attributes
**dist (binprism.PPD):** *Probability distribution that events follow* <br />
**total (numeric):** *Total number of events* <br />
**time_range (tuple):** *Length-2 tuple indicating the start and end times of one period of events* <br />
**mean_time (float):** *Mean time that events occur in the units defined by* `time_range`

## Methods
[angle2time](angle2time.md) <br />
[count_events](count_events.md) <br />
[eval](eval.md) <br />
[plot](plot.md) <br />
[shift](shift.md) <br />
[sim](sim.md) <br />
[time2angle](time2angle.md) <br />
[time2hhmm](time2hhmm.md) <br />

## Example
```
>>> fs = bp.FourierSeries([-2, 0.5j, 0.1 - 0.2j, 0.05 + 0.05j])
>>> dist = bp.PPD(fs)
>>> total_events = 1000
>>> time_range = (0, 24)
>>> profile = bp.Profile(dist, total_events, time_range)
>>> profile
binprism.Profile
Total Events: 1000.0
Time Range:  (0, 24)
Mean Time: 17.137893225691656
PDF: f(x) = exp(-2.1182135495889716 + (0.0)cos(x) + (-1.0)sin(x) + (0.2)cos(2x) + (0.4)sin(2x) + (0.1)cos(3x) + (-0.1)sin(3x))
>>> profile[24] #Events in each hour
array([  39.12382631,   31.10838045,   23.37826631,   17.54597888,
         13.697433  ,   11.31280299,    9.92586336,    9.35611125,
          9.76048449,   11.72434122,   16.57731333,   26.90133913,
         46.15266808,   74.46367083,  101.35159174,  109.80080641,
         96.08266643,   73.7161064 ,   55.6976585 ,   45.81392818,
         42.71632191,   43.74720067,   45.53542367,   44.50984576])
>>> profile[15:18] #Events between 3 and 6 pm
279.59957924186853
>>> profile[15:18:0.25] #Events between 3 and 6 pm in 15-minute intervals
array([ 27.63582213,  27.77404247,  27.51044347,  26.88049834,
        25.9402149 ,  24.75896753,  23.4117015 ,  21.9717825 ,
        20.50540596,  19.06800389,  17.70263948,  16.44005707])
>>> profile.plot(N = 250, color = 'b', linewidth = 2)
>>> plt.xticks(range(0, 25, 3))
>>> plt.xlabel('Hour of Day')
>>> plt.ylabel('Events per Hour')
>>> plt.grid(True)
>>> plt.xlim(time_range)
>>> plt.show()
```
![alt text](ProfileExample.png "binprism.Profile example")
