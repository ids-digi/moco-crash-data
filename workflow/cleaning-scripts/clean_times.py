""" 
this script cleans the date/time for crash data from 2013-2018 and 2003-2015
it cleans the times and prepares the `Collision Date` and `Collision Time`
columns for the `clean_datetime.py` script

"""
import sys 

import pandas as pd
import numpy as np
from datetime import date, time
import re

def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset. """
    return pd.read_csv(in_file)

def clean_times_1318(Time):
    # Search for 3- or 4-digit times
    # these are in military time. so need to be converted to regular time to match the rest.
    if re.search('\d{3,4}', Time):
        
        # ex 1230, 1024
        if len(Time) == 4:
            if int(Time[0:2])>12:
                return str(int(Time[0:2]) - 12) + ":" + Time[2:4] + " PM"
            elif Time[0:2] == '12':
                return Time[0:2] + ":" + Time[2:4] + " PM"
            else:
                return Time[0:2] + ":" + Time[2:4] + " AM"
            
        # ex 130, 930, 725
        if len(Time) == 3:
            if Time[0:1] == '0':
                return "12:" + Time[1:3] + " AM"
            else:
                return Time[0:1] + ":" + Time[1:3] + " AM" 
        return Time
    else:
        # if clean up not needed, return the same name
        return Time

# remove all times with one or two digit numbers 
def find_wrong_times_1318(Time):
    if not re.search('\d{1,2}:\d{2} [A,P]M', Time):
        return float('NaN')
    else:
        return Time
    
def clean_1318(df, time_col):
    df[time_col] = df[time_col].apply(clean_times_1318)
    df[time_col] = df[time_col].apply(find_wrong_times_1318)
    return df

def clean_time_0315(hour_string):
    # test if float exists
    if hour_string == hour_string:
        return str(time(int(hour_string / 100)))

def clean_0315(df):
    df['Collision Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df['Collision Time'] = df['Hour'].apply(clean_time_0315)
    return df.drop(columns=['Year','Month','Day','Hour','Weekend?'])

def save_clean_df(cleaned_df, out_file):
    ''' save the cleaned df '''
    cleaned_df.to_csv(out_file, index=False)

if __name__ == "__main__":
    DF_13_18 = load_data(sys.argv[1])
    DF_03_15 = load_data(sys.argv[2])
    OUTFILE1 = sys.argv[3]
    OUTFILE2 = sys.argv[4]

    CLEAN_DF1 = clean_1318(DF_13_18, 'Collision Time')
    CLEAN_DF2 = clean_0315(DF_03_15)
    save_clean_df(CLEAN_DF1,OUTFILE1)
    save_clean_df(CLEAN_DF2,OUTFILE2)

    """
    run this command in the terminal: 
    
    python clean_times.py "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"  
    """