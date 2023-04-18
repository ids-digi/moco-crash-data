# Monroe County crash data cleaning scripts

`cd` into the `cleaning-scripts` folder in the terminal and run these scripts in order to execute all cleaning scripts:

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
python clean_datetime.py "../../source-data/moco-crash-2022.csv" "../../data-output/clean_date_times/moco-crash-2022.csv" /
python clean_datetime.py "../../source-data/moco-crash-2021.csv" "../../data-output/clean_date_times/moco-crash-2021.csv" /
python clean_datetime.py "../../source-data/moco-crash-2020.csv" "../../data-output/clean_date_times/moco-crash-2020.csv" /
python clean_datetime.py "../../source-data/moco-crash-2019.csv" "../../data-output/clean_date_times/moco-crash-2019.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/clean_date_times/moco-crash-2013-2018.csv" /
python clean_datetime.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/clean_date_times/moco-crash-2003-2015.csv"
```
4. clean the addresses
```curl
```

OR you can run them all at once: 
```curl
python main_data_cleaning.py "../../source-data/moco-crash-2013-2018.csv" "../../source-data/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" /
python clean_times.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"  /
python clean_datetime.py "../../source-data/moco-crash-2022.csv" "../../data-output/clean_date_times/moco-crash-2022.csv" /
python clean_datetime.py "../../source-data/moco-crash-2021.csv" "../../data-output/clean_date_times/moco-crash-2021.csv" /
python clean_datetime.py "../../source-data/moco-crash-2020.csv" "../../data-output/clean_date_times/moco-crash-2020.csv" /
python clean_datetime.py "../../source-data/moco-crash-2019.csv" "../../data-output/clean_date_times/moco-crash-2019.csv" / 
python clean_datetime.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/clean_date_times/moco-crash-2013-2018.csv" /
python clean_datetime.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/clean_date_times/moco-crash-2003-2015.csv"
```
