# binprism.Profile
***`binprism.Profile(dist, total, time_range)`*** <br />
*dist (binprism.PPD): Probability distribution that events follow* <br />
*total (numeric): Total number of events* <br />
*time_range (tuple): Length-2 tuple indicating the start and end times of one period of events* <br />
A profile of events distributed throughout a time period, such as events throughout the day or year.

## Attributes
*dist (binprism.PPD): Probability distribution that events follow* <br />
*total (numeric): Total number of events* <br />
*time_range (tuple): Length-2 tuple indicating the start and end times of one period of events* <br />
*mean_time (float): Mean time that events occur in the units defined by* `time_range`

## Methods
angle2time
count_events
eval
plot
shift
sim
time2angle
time2hhmm
