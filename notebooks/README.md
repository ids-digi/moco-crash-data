# Monroe County crash data notebooks
*These notebooks describe the cleaning process and basic exploration of the Monroe County crash data. For finalized cleaning scripts, view the [`cleaning-workflow`](../cleaning-workflow) folder, which has more information on how to run the scripts yourself.*

[**1. explore data and caveats**](1.%20explore%20data%20and%20caveats.ipynb)

This script gives a first look at the fields in the different datasets and explains some caveats with the data.

[**2. cleaning dates + times**](2.%20cleaning%20dates%20%2B%20times.ipynb)

This script explains how the dates and times are cleaned and standardized for each [source file](../data/source-data/) in the [cleaning scripts](../cleaning-workflow/cleaning-scripts/).

[**3. cleaning addresses**](3.%20cleaning%20addresses.ipynb)

This script explains the process for cleaning and standardizing road addresses to allow for intersection analysis.

[**4. comparing fatalities and injuries**](4.%20comparing%20fatalities%20and%20injuries.ipynb)

This script explains the process for comparing fatalities and injuries across datasets for years of data that were logged differently. 

[**5. looking at trends from clean data**](5.%20looking%20at%20trends%20from%20clean%20data.ipynb)

Using the cleaned data, this script looks at a few trends to show how the data can be visualized with Python.
