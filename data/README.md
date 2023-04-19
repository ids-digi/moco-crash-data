# Data

This folder includes all the source data and clean data output from the [cleaning-scripts](../cleaning-workflow/cleaning-scripts/). 

## Benefits/drawbacks of the data sets
1. `master-crashes.csv`
This data file is useful in that it combines all the data from 2003 to 2022 and allows you to map or visualize trends from all these years at once. **But**, combining data from years when it was collected differently presents issues and caveats. The main issue is that the `Number Dead` and `Number Injured` columns for the years 2003-2012 are low estimates. If a row in one of these years has `Number Injured` listed as `1`, this means there was `at least 1` injury, and might have been more. While useful to distinguish between crash severity in a mapping or trend-visualizing context, this means that the total number of injuries or deaths from the years 2003-2012 is definitely inaccurate. 

The `master-crashes.csv` file also has fewer columns in the interest of keeping the file size smaller and only keeping useful columns that can be compared. Analysis of columns that are excluded, such as the `Pedestrian Involved` column only available for years 2003-2015, could definitely still provide useful analysis but aren't included in this master file. 

Another caveat is that there is overlap in the source data for years 2012-2015. The source files `moco-crash-2003-2015.csv` and `moco-crash-2013-2013.csv` both contain data for years 2012-2015. In the interest of avoiding duplicates and keeping the most accurate fatality and injury numbers, years 2012-2015 were dropped from `moco-crash-2003-2015.csv` to create this master file. 

2. `moco-crash-2022-clean.csv`, `moco-crash-2021-clean.csv`, `moco-crash-2021-clean.csv`, `moco-crash-2020-clean.csv`, `moco-crash-2019-clean.csv`
These data files all share the same columns, which are explained in detail in the [data dictionary](../README.md#data-dictionary). It can be useful to compare these years since they were definitely created using the same reporting process. They have the most fields compared with previous years, but they do lack a field showing pedestrian or cyclist involvement. 

3. `moco-crash-2013-2018-clean.csv`
This file contains data from years 2013-2018. Its fields are pretty similar to the data sets described above, but there are not quite as many fields. Overall it is quite comparable to the above years. 

4. `moco-crash-2003-2015-clean.csv`
This file is quite different from the other years of data. The main drawback is it includes way fewer fields (as explained in the [data dictionary](../README.md#fields-for-source-data-from-2003-2015)), but it has the advantage of including more details about pedestrian and cyclist involvement, as well as bus involvement. There is also more specificity about how severe injuries were. Fatality and injury counts from these years should be taken as an estimate. 