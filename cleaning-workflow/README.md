# Monroe County crash data cleaning scripts

`cd` into the `cleaning-scripts` folder in the terminal and run these scripts in order to execute all cleaning scripts:

## Option 1: run the scripts one by one

1. main data cleaning
```curl
python main_data_cleaning.py "../../source-data/moco-crash-2013-2018.csv" "../../source-data/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"
```
2. clean the times
```curl
python clean_times.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"  
```
3. produce `DateTime` column in each dataset
```curl
python clean_datetime.py "../../source-data/moco-crash-2022.csv" "../../data-output/temp/moco-crash-2022.csv" /
python clean_datetime.py "../../source-data/moco-crash-2021.csv" "../../data-output/temp/moco-crash-2021.csv" /
python clean_datetime.py "../../source-data/moco-crash-2020.csv" "../../data-output/temp/moco-crash-2020.csv" /
python clean_datetime.py "../../source-data/moco-crash-2019.csv" "../../data-output/temp/moco-crash-2019.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2013-2018.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2003-2015.csv"
```
4. clean the addresses
```curl
python clean_addresses.py "../../data-output/temp/moco-crash-2022.csv" "../../data-output/clean_files/moco-crash-2022.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2021.csv" "../../data-output/clean_files/moco-crash-2021.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2020.csv" "../../data-output/clean_files/moco-crash-2020.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2019.csv" "../../data-output/clean_files/moco-crash-2019.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/clean_files/moco-crash-2013-2018.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/clean_files/moco-crash-2003-2015.csv" 
```
5. combine into master file for mapping 

*to compare data across years, this step requires estimating the death/injury counts from 2003-2015, which reported these values differently than future reports. this means that death/injury estimates for 2003-2012 are likely low estimates, because the original data records injuries/crashes as a true/false value, rather than indicating how many occurred. for mapping purposes, the below scripts encode all `true` values as 1 death or injury, and all `false` values as 0 deaths or injuries.*
```curl
python make_master_file.py "../../data-output/temp/moco-crash-2022.csv" "../../data-output/temp/moco-crash-2021.csv" "../../data-output/temp/moco-crash-2020.csv" "../../data-output/temp/moco-crash-2019.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/master-crashes.csv"
```

## Option 2: run them all at once
Just copy the below code and paste it into terminal
```curl
python main_data_cleaning.py "../../source-data/moco-crash-2013-2018.csv" "../../source-data/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" /
python clean_times.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"  /
python clean_datetime.py "../../source-data/moco-crash-2022.csv" "../../data-output/temp/moco-crash-2022.csv" /
python clean_datetime.py "../../source-data/moco-crash-2021.csv" "../../data-output/temp/moco-crash-2021.csv" /
python clean_datetime.py "../../source-data/moco-crash-2020.csv" "../../data-output/temp/moco-crash-2020.csv" /
python clean_datetime.py "../../source-data/moco-crash-2019.csv" "../../data-output/temp/moco-crash-2019.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2013-2018.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2003-2015.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2022.csv" "../../data-output/clean_files/moco-crash-2022.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2021.csv" "../../data-output/clean_files/moco-crash-2021.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2020.csv" "../../data-output/clean_files/moco-crash-2020.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2019.csv" "../../data-output/clean_files/moco-crash-2019.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/clean_files/moco-crash-2013-2018.csv" /
python clean_addresses.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/clean_files/moco-crash-2003-2015.csv" /
python make_master_file.py "../../data-output/temp/moco-crash-2022.csv" "../../data-output/temp/moco-crash-2021.csv" "../../data-output/temp/moco-crash-2020.csv" "../../data-output/temp/moco-crash-2019.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/master-crashes.csv" 
```
