# Monroe County crash data cleaning scripts

`cd` into the `cleaning-scripts` folder in the terminal and run these scripts in order to execute all cleaning scripts.

For more information about how the data was cleaned, look at the [`notebook`](../notebooks) folder, which has annotated Jupyter notebooks describing the thought process behind each cleaning step.

## Option 1: run the scripts one by one

1. main data cleaning
```curl
python main_data_cleaning.py "../../data/source-data/moco-crash-2013-2018.csv" "../../data/source-data/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv"
```
2. clean the times
```curl
python clean_times.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv"  
```
3. produce `DateTime` column in each dataset
```curl
python clean_datetime.py "../../data/source-data/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" / 
python clean_datetime.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" / 
python clean_datetime.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" /
python clean_datetime.py "../../data/source-data/bike-crashes-2013-2023.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" /
python clean_datetime.py "../../data/source-data/ped-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv"
```
4. clean the addresses
```curl
python clean_addresses.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/clean-data/moco-crash-2003-2015-clean.csv" /
python clean_addresses.py "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" /
python clean_addresses.py "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv"
```

5. update geocoding with more accurate lat/lon data
```curl
python geocode.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" 
```

6. merge the bike/ped information into the master files for 2013-2018
```curl
python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2022-clean.csv" /

python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2021-clean.csv" /

python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2020-clean.csv" /

python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2019-clean.csv" /
```

7. combine into master file for mapping 
This step takes a really long time to run. It might take longer than an hour if you clean every file. If you are working on analysis that doesn't require accurate lat/lon data, you can skip this step. 

*to compare data across years, this step requires estimating the death/injury counts from 2003-2015, which reported these values differently than future reports. this means that death/injury estimates for 2003-2012 are likely low estimates, because the original data records injuries/crashes as a true/false value, rather than indicating how many occurred. for mapping purposes, the below scripts encode all `true` values as 1 death or injury, and all `false` values as 0 deaths or injuries.*
```curl
python make_master_file.py "../../data/clean-data/moco-crash-2022-clean.csv" "../../data/clean-data/moco-crash-2021-clean.csv" "../../data/clean-data/moco-crash-2020-clean.csv" "../../data/clean-data/moco-crash-2019-clean.csv" "../../data/clean-data/moco-crash-2013-2018-clean.csv" "../../data/clean-data/moco-crash-2003-2015-clean.csv" "../../data/clean-data/master-crashes.csv"
```

## Option 2: run them all at once
Just copy the below code and paste it into terminal:
```curl
python main_data_cleaning.py "../../data/source-data/moco-crash-2013-2018.csv" "../../data/source-data/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" /
python clean_times.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv"  /
python clean_datetime.py "../../data/source-data/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python clean_datetime.py "../../data/source-data/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" / 
python clean_datetime.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" / 
python clean_datetime.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" /
python clean_datetime.py "../../data/source-data/bike-crashes-2013-2023.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" /
python clean_datetime.py "../../data/source-data/ped-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" /
python clean_addresses.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/clean-data/moco-crash-2003-2015-clean.csv" /
python clean_addresses.py "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" /
python clean_addresses.py "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/moco-crash-2022.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/moco-crash-2021.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/moco-crash-2020.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/moco-crash-2019.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2013-2018.csv" "../../data/cleaning-process/moco-crash-2013-2018.csv" /
python geocode.py "../../data/cleaning-process/moco-crash-2003-2015.csv" "../../data/cleaning-process/moco-crash-2003-2015.csv" /
python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2022.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2022-clean.csv" /
python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2021.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2021-clean.csv" /
python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2020.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2020-clean.csv" /
python merge_bike_ped.py "../../data/cleaning-process/moco-crash-2019.csv" "../../data/cleaning-process/bike-crashes-2013-2023.csv" "../../data/cleaning-process/ped-crashes-2013-2023.csv" "../../data/clean-data/moco-crash-2019-clean.csv" /
python make_master_file.py "../../data/clean-data/moco-crash-2022-clean.csv" "../../data/clean-data/moco-crash-2021-clean.csv" "../../data/clean-data/moco-crash-2020-clean.csv" "../../data/clean-data/moco-crash-2019-clean.csv" "../../data/clean-data/moco-crash-2013-2018-clean.csv" "../../data/clean-data/moco-crash-2003-2015-clean.csv" "../../data/clean-data/master-crashes.csv"
```