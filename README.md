# Monroe County crash data 

*Repository to show the source data, data cleaning and data exploration that went into the IDS Monroe County Crash Dashboard published in May 2023.*
*Special thanks to YY Ahn, Mike Stewart, Ryan Clemens & Mark Stosberg for help on this project*

## [notebooks](https://github.com/ids-digi/moco-crash-data/tree/main/notebooks)
This folder contains Python notebooks which explain the caveats of the data, explore basic trends and show the process that went into cleaning the data to prepare it for mapping. We hope these notebooks will help people who are trying to explore this data themselves understand it better and have a starting point to learn more.

## [cleaning-workflow](https://github.com/ids-digi/moco-crash-data/tree/main/cleaning-workflow)
This folder contains the cleaning scripts which produce the clean data from the [source data](https://github.com/ids-digi/moco-crash-data/tree/main/data/source-data). There are instructions within the `readme` in this folder which explain how to run the cleaning scripts on your own computer. The logic that went into the cleaning scripts is explained in the [notebooks](https://github.com/ids-digi/moco-crash-data/tree/main/notebooks) folder.

## [data](https://github.com/ids-digi/moco-crash-data/tree/main/data)
This folder contains the source data from [Bloomington Open Data](https://data.bloomington.in.gov/dataset/traffic-data), and a [data dictionary](https://github.com/ids-digi/moco-crash-data/tree/main/data#data-dictionary) which explains all the fields from the source data. It also includes the [clean-data](https://github.com/ids-digi/moco-crash-data/tree/main/data/clean-data) which has already been standardized and cleaned with the [cleaning-workflow](https://github.com/ids-digi/moco-crash-data/tree/main/cleaning-workflow). Finally, the [cleaning-process](https://github.com/ids-digi/moco-crash-data/tree/main/data/cleaning-process) folder stores partially cleaned data during the data process.

# Methodology
- Crash data is reported by local law enforcement, aggregated at the state level by the Indiana State Police and then sent back to county officials. Map data includes all reported crashes in Monroe County from 2003-2022.
-Fatalities and injuries are estimates for years 2003-2012, because those years were reported through a different system. A fatality or injury of 1 for a crash prior to 2013 means there was at least one reported fatality or injury. 
- Crashes in the database only include those that were reported to law enforcement. Most often, this means that law enforcement was at the scene or that people involved in the crash notified law enforcement afterward for insurance purposes. This means that many minor crashes are not accounted for in the data.
- Street addresses input by police often include typos or mistakes. Latitude and longitude data in the public dataset is also often incorrect as a result. The IDS cleaned the crash data to improve the accuracy of the addresses and the locations of the dots, but there are still errors in the map. The intersection listed when hovering over a crash dot is the most accurate way to see where the original crash was, rather than the actual location of the dot on the map.
- Overlapping crash dots have been moved slightly to allow them to be seen on the map. This means that the location of each dot is not exactly where the crash occurred, but is still within a few meters of the original intersection.
Base data is from the Bloomington open data portal, which provides crash data from 2003-2021 and partial data for 2022. The - Bloomington Planning and Transportation Department provided the full dataset for 2022 and data for crashes that involved cyclists or pedestrians.
- Pedestrian and cyclist crashes are more likely to be underreported, according to city officials. This is because collisions between vehicles are more likely to result in material damage that is reported to law enforcement for insurance purposes. 
*Special thanks to YY Ahn, Mike Stewart, Vivien Ngo and Mark Stosberg for their expertise and help on the data cleaning and map.*

