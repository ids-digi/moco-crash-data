# Monroe County crash data 

*Repository to show the source data, data cleaning and data exploration that went into the IDS Monroe County Crash Dashboard published in May 2023.*
*Special thanks to YY Ahn, Mike Stewart, Ryan Clemens & Mark Stosberg for help on this project*

## [notebooks](notebooks)
This folder contains Python notebooks which explain the caveats of the data, explore basic trends and show the process that went into cleaning the data to prepare it for mapping. We hope these notebooks will help people who are trying to explore this data themselves understand it better and have a starting point to learn more.

## [cleaning-workflow](cleaning-workflow)
This folder contains the cleaning scripts which produce the clean data from the [source data](source-data). There are instructions within the `readme` in this folder which explain how to run the cleaning scripts on your own computer. The logic that went into the cleaning scripts is explained in the [notebooks](notebooks) folder.

## [data](data)
This folder contains the source data from [Bloomington Open Data](https://data.bloomington.in.gov/dataset/traffic-data), and a [data dictionary](data/README.md#data-dictionary) which explains all the fields from the source data. It also includes the [clean-data](data/clean-data/) which has already been standardized and cleaned with the [cleaning-workflow](cleaning-workflow). Finally, the [cleaning-process](data/cleaning-process/) folder stores partially cleaned data during the data process.
