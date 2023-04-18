""" 
this script cleans the date/time for crash data from 2016 - 2022
given two columns `Collision Date` and `Collision Time`, it returns
one column called `DateTime`

"""
import sys 

import pandas as pd
import numpy as np
from datetime import date, time

def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset. """
    return pd.read_csv(in_file)

# given a date string (`Collision Date` field) and a time string (`Collision Time` field),,,
def get_datetime(date_string, time_string):
    # combine the date and time into one `datetime` object
    date_val = date(
        pd.to_datetime(date_string).year,
        pd.to_datetime(date_string).month,
        pd.to_datetime(date_string).day,
    )
    if time_string:
        # if the time string is `NaN`, set it to midnight
        try:
            time_val = time(
                pd.to_datetime(time_string).hour, pd.to_datetime(time_string).minute
            )
        except:
            time_val = time(0, 0, 0)

    return pd.Timestamp.combine(date_val, time_val)

def clean_date_time(df, date_column, time_column):
    df['DateTime'] = df.apply(lambda row: get_datetime(row[date_column], row[time_column]), axis=1)
    df = df.drop(columns=[date_column, time_column])
    return df

def save_clean_df(cleaned_df, out_file):
    ''' save the cleaned df '''
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":
    # DF = load_data("./source-data/moco-crash-2022.csv")
    DF = load_data(sys.argv[1])
    OUTFILE = sys.argv[2]

    # print('running datetime script with ' + sys.argv[1] + ' and ' + sys.argv[2])

    CLEAN_DF = clean_date_time(DF, 'Collision Date', 'Collision Time')
    save_clean_df(CLEAN_DF,OUTFILE)

    """
    run this command in the terminal: 

    python clean_datetime.py "../../source-data/moco-crash-2022.csv" "../../data-output/clean_date_times/moco-crash-2022.csv" /
    python clean_datetime.py "../../source-data/moco-crash-2021.csv" "../../data-output/clean_date_times/moco-crash-2021.csv" /
    python clean_datetime.py "../../source-data/moco-crash-2020.csv" "../../data-output/clean_date_times/moco-crash-2020.csv" /
    python clean_datetime.py "../../source-data/moco-crash-2019.csv" "../../data-output/clean_date_times/moco-crash-2019.csv" / 
    python clean_datetime.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/clean_date_times/moco-crash-2013-2018.csv" / 
    python clean_datetime.py "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/clean_date_times/moco-crash-2003-2015.csv"
    """