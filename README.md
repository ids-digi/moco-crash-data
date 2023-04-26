# Monroe County crash data 

*Repository to show the source data, data cleaning and data exploration that went into the IDS Monroe County Crash Dashboard published in May 2023.*
*Special thanks to YY Ahn, Mike Stewart, Ryan Clemens & Mark Stosberg for help on this project*

## [notebooks](notebooks)
This folder contains Python notebooks which explain the caveats of the data, explore basic trends and show the process that went into cleaning the data to prepare it for mapping. We hope these notebooks will help people who are trying to explore this data themselves understand it better and have a starting point to learn more.

## [cleaning-workflow](cleaning-workflow)
This folder contains the cleaning scripts which produce the clean data from the [source data](source-data). There are instructions within the `readme` in this folder which explain how to run the cleaning scripts on your own computer. The logic that went into the cleaning scripts is explained in the [notebooks](notebooks) folder.

## [data](data)
This folder contains the source data from [Bloomington Open Data](https://data.bloomington.in.gov/dataset/traffic-data). It also includes the [clean-data](data/clean-data/) which has already been standardized and cleaned with the [cleaning-workflow](cleaning-workflow). Finally, the [cleaning-process](data/cleaning-process/) folder stores partially cleaned data during the data process.

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
