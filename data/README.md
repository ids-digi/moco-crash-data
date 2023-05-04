# Data

This folder includes all the source data and clean data output from the [cleaning-scripts](../cleaning-workflow/cleaning-scripts/). 

The source data is from [Bloomington Open Data](https://data.bloomington.in.gov/dataset/traffic-data).

## Benefits/drawbacks of the datasets
1. [`master-crashes.csv`](clean-data/master-crashes.csv)

This data file is useful in that it combines all the data from 2003 to 2022 and allows you to map or visualize trends from all these years at once. **But**, combining data from years when it was collected differently presents issues and caveats. The main issue is that the `Number Dead` and `Number Injured` columns for the years 2003-2012 are low estimates. If a row in one of these years has `Number Injured` listed as `1`, this means there was `at least 1` injury, and might have been more. While useful to distinguish between crash severity in a mapping or trend-visualizing context, this means that the total number of injuries or deaths from the years 2003-2012 is definitely inaccurate. 

The `master-crashes.csv` file also has fewer columns in the interest of keeping the file size smaller and only keeping useful columns that can be compared. Analysis of columns that are excluded, such as the `Pedestrian Involved` column only available for years 2003-2015, could definitely still provide useful analysis but aren't included in this master file. 

Another caveat is that there is overlap in the source data for years 2012-2015. The source files `moco-crash-2003-2015.csv` and `moco-crash-2013-2013.csv` both contain data for years 2012-2015. In the interest of avoiding duplicates and keeping the most accurate fatality and injury numbers, years 2012-2015 were dropped from `moco-crash-2003-2015.csv` to create this master file. 

2. [`moco-crash-2022-clean.csv`](clean-data/moco-crash-2022-clean.csv), [`moco-crash-2021-clean.csv`](clean-data/moco-crash-2021-clean.csv), [`moco-crash-2020-clean.csv`](clean-data/moco-crash-2020-clean.csv), [`moco-crash-2019-clean.csv`](clean-data/moco-crash-2019-clean.csv)

These data files all share the same columns, which are explained in detail in the [data dictionary](../README.md#data-dictionary). It can be useful to compare these years since they were definitely created using the same reporting process. They have the most fields compared with previous years, but they do lack a field showing pedestrian or cyclist involvement. 

3. [`moco-crash-2013-2018-clean.csv`](clean-data/moco-crash-2013-2018-clean.csv)

This file contains data from years 2013-2018. Its fields are pretty similar to the data sets described above, but there are not quite as many fields. Overall it is quite comparable to the above years. 

4. [`moco-crash-2003-2015-clean.csv`](clean-data/moco-crash-2003-2015-clean.csv)

This file is quite different from the other years of data. The main drawback is it includes way fewer fields (as explained in the [data dictionary](../README.md#fields-for-source-data-from-2003-2015)), but it has the advantage of including more details about pedestrian and cyclist involvement, as well as bus involvement. There is also more specificity about how severe injuries were. Fatality and injury counts from these years should be taken as an estimate. 

## Data dictionary
This is a data dictionary which provides more information on what each field of the public data means. The dictionary is based on interviews with Bloomington city employees. 

The public datasets are compiled by the Indiana State Police based on reports from law enforcement from jurisdictions across the state. The crash data only includes crashes that were reported to law enforcement in some way. This typically means that either police show up at the scene of the crash, or the people involved in the crash report it to the sheriff's office later for insurance purposes. 

### Fields for source data from 2019-2022

Field name | Description
----------|------------
Agency | Which agency reported the crash. Most frequently `BLOOMINGTON PD`, `MONROE SD`, `INDIANA UNIV BLOOMINGTON PD`, `ISP BLOOMINGTON 33` or `ELLETTSVILLE PD`
City | In which city the crash was reported. Most often `BLOOMINGTON` or `ELLETTSVILLE`
Collision Date | Date the collision happened (string)
Collision Time | Time the collision happened (string)
Vehicles Involved | How many vehicles were involved (integer)
Trailers Involved | How many trailers were involved (integer)
Number Injured | How many people were injured in the crash (integer)
Number Dead | How many people died in the crash (integer)
Number Deer | How many deer were involved in the crash (integer)
House Number | The house number of the nearest building to where the crash happened. Rarely included, and typically included when there is not a nearby intersecting road.
Roadway Interchange | Almost never noted. Typically indicates the mile marker nearest to a crash that happened on a state road.
Roadway Ramp | Almost never noted. Typically refers to the ID of a ramp leading onto/off of a state road or highway.
Roadway Id | One of the roads, or the only road, where the crash happened. In crashes involving two roads (intersection), law enforcement use different criteria to determine which one is listed as the Roadway Id and which one is listed as the Intersecting Road. Some people list the road where the car originated, where the car at fault was driving, or the bigger of the two roads at the intersection.
Intersecting Road | The second road involved in the crash, if it happened at an intersection. In some cases, law enforcement might note the intersecting road even if the crash happened a few hundred feet away. 
Interchange | Empty field
Feet From | Approximated by officer, and might mean different things. Sometimes omitted. Some officers use it to indicate how far away the crash was from the intersection noted in the `Roadway Id` and `Intersecting Road` columns. City employees assume about 200 feet of error when using this field.
Direction | Either the way the vehicle was heading, or the direction used in the `Feet From` column when estimating how far the crash was from an intersection (officer discretion).
Latitude | Latitude of the crash. Usually automatically geocoded based on the `Roadway Id` and `Intersecting Road` fields.
Longitude | Longitude. Also geocoded.
Roadway Class | Type of road. Either `INTERSTATE`, `STATE ROAD`, `LOCAL/CITY ROAD`, `COUNTY ROAD`, `PRIVATE DRIVE` or `OTHER`.
Hit and Run? | Often left blank. If filled in, it's either `N` for not a hit and run, or `Y` for a hit and run.
Locality | Either `RURAL` or `URBAN`
School Zone? | `Y` if the crash occurred in a school zone, `N` if not
Rumble Strips? | `Y` if there were rumble strips at the site of the crash, `N` if not
Construction? | Rarely filled out. `N` or `Y` to indicate whether or not there was construction.
Construction Type | Also rarely filled out. If it is, the options are `INTERMITTENT OR MOVING WORK`, `LANE CLOSURE`, `WORK ON SHOULDER` or `X-OVER/LANE SHIFT`
Light Condition | `DARK (NOT LIGHTED)`, `DAWN/DUSK`, `DAYLIGHT`, `DARK (LIGHTED)` or `UNKNOWN`
Weather Conditions | `CLEAR`, `CLOUDY`, `RAIN`, `FOG/SMOKE/SMOG`, `SNOW`, `SLEET/HAIL/FREEZING RAIN`, `BLOWING SAND/SOIL/SNOW`
Surface Condition | `DRY`, `ICE`, `WET`, `WATER (STANDING OR MOVING)`, `SNOW/SLUSH`, `LOOSE MATERIAL ON ROAD`, `MUDDY`
Type of Median | Empty field
Roadway Junction Type | `NO JUNCTION INVOLVED`, `T-INTERSECTION`, `FOUR-WAY INTERSECTION`, `TRAFFIC CIRCLE/ROUNDABOUT`, `RAMP`, `INTERCHANGE`, `Y-INTERSECTION`, `RAILROAD CROSSINGS`, `TRAIL CROSSINGS`, `FIVE POINT OR MORE`
Road Character | Rarely filled out. If it is, options are: `STRAIGHT/GRADE`, `CURVE/LEVEL`, `CURVE/HILLCREST`, `STRAIGHT/LEVEL`, `STRAIGHT/HILLCREST`, `CURVE/GRADE` or `NON-ROADWAY CRASH`
Roadway Surface | `ASPHALT`, `CONCRETE`, `GRAVEL` or `OTHER - EXPLAIN IN NARRATIVE`
Primary Factor | The main reason the crash happened. 
Manner of Collision | How the crash happened, ex. `ran off road`, `left turn`.
Unique Location Id | Automatically generated field which combines `Roadway Id` and `Intersecting Road`
Traffic Control | Rarely filled out. If so, options are: `NONE`, `LANE CONTROL`, `TRAFFIC CONTROL SIGNAL`, `YIELD SIGN`, `STOP SIGN`, `OTHER`, `OTHER REGULATORY SIGN/MARKING`

### Fields for source data from 2013-2018
*Duplicate fields are not included*
Field name | Description
----------|------------
DATE | Same as `Collision Date` above
TIME | Same as `Collision Time` above
VEH# | Same as `Vehicles Involved` above
DEAD | Same as `Number Dead` above
DEER | Same as `Number Deer` above
House# | Same as `House Number` above
Intersect Rd. | Same as `Intersecting Road` above
Interchange | Rarely included. If so, indicates the mile marker or the name of the highway.
Dir | Same as `Direction` above
H&R | Same as `Hit and Run?` above
School | Same as `School Zone?` above
CN Zone | Same as `Construction?` above
CN Type | Same as `Construction Type` above
Light | Same as `Light Condition` above
Weather | Same as `Weahter Conditions` above
Surf Con | Same as `Surface Condition` above
Road Char | Same as `Road Character` above
Surface | Same as `Roadway Surface` above
Collision Type | Same as `Manner of Collision` above
Unique Id | Same as `Unique Location Id` above

## Fields for source data from 2003-2015
*Duplicate fields are not included*
Field name | Description
----------|------------
Master Record Number | 9-digit ID number for each record
Year | Year when the crash happened (integer)
Month | Month when the crash happened (integer)
Day | Day of the week when the crash happened (integer) 
Weekend? | If the crash happened on a weekend. Possible values: `Weekday`, `Weekend`
Hour | Hour of the day when the crash happened (float). Ex. `2300` means `11 PM`
Collision Type | Combination of `Vehicle Number` field from above, along with information about pedestrian/cyclist/motorist involvement. Possible values: `2-Car`, `1-Car`, `3+ Cars`, `Pedestrian`, `Cyclist`, `Bus`, `Moped/Motorcycle`
Injury Type | Combination of `Number Injured` and `Number Dead` fields from above, with different information. Possible values: `No injury/unknown`, `Non-incapacitating`, `Incapacitating`, `Fatal`
Reported_Location | A combination of `Roadway Id` and `Intersecting Road`. If there are two roads involved, they are connected with a `&` symbol. 
