""" 
this script standardizes the column names of the raw crash data
input:
    - moco-crash-2013-2018.csv
    - moco-crash-2003-2015.csv
output:
    - data-output/temp/moco-crash-2013-2018.csv
    - data-output/temp/moco-crash-2003-2015.csv
"""
import sys 

import pandas as pd
import re

def load_data(crash_file):
    """ returns a pandas dataframe of the raw dataset. """
    return pd.read_csv(crash_file,encoding='unicode_escape')

def rename_df(crash_df, rename_dict):
    """ renaming columns to match with 2019-2022 field names """
    return crash_df.rename(index=str, columns=rename_dict, inplace=False)

def get_road1(row):
    if isinstance(row, str):
        return row.split("&")[0].strip()
    else:
        return ''
def get_road2(row):
    if isinstance(row,str):
        return row.split("&")[1] if len(row.split("&")) > 1 else ''
        
    else:
        return ''
# remove all info in parentheses in street names
def remove_parens(row):
    return " ".join(re.sub('\(.*\)', '', row).split())

def organize_location_cols(df):
    df['Roadway Id'] = df['Reported_Location'].apply(get_road1)
    df['Intersecting Road'] = df['Reported_Location'].apply(get_road2)

    df['Roadway Id'] = df['Roadway Id'].fillna('')
    df['Intersecting Road'] = df['Intersecting Road'].fillna('')

    df['Roadway Id'] = df['Roadway Id'].apply(remove_parens)
    df['Intersecting Road'] = df['Intersecting Road'].apply(remove_parens)
    return df.drop(columns=["Reported_Location"])

def save_clean_df(cleaned_df, out_file):
    ''' save the cleaned df '''
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":

    rename_dict_13_18 = {
        "DATE": "Collision Date", 
        "TIME": "Collision Time", 
        "Trailers": "Trailers Involved",
        "INJ": "Number Injured",
        "DEAD": "Number Dead",
        "DEER": "Number Deer",
        "House#": "House Number",
        "VEH#": "Vehicles Involved",
        "Surf Con": "Surface Condition",
        "Collision Type": "Manner of Collision",
        "Rd Junction": "Roadway Junction Type",
        "Weather": "Weather Conditions",
        "Road Char": "Road Character",
        "Surface": "Roadway Surface",
        "CN Zone": "Construction?",
        "Unique Id": "Unique Location Id",
        'Intersect Rd.': "Intersecting Road"
        }
    rename_dict_03_15 = {
        "Collision Type": "Vehicles Involved"
    }

    # DF_13_18 = load_data("./source-data/moco-crash-2013-2018.csv")
    # DF_03_15 = load_data("./source-data/moco-crash-2003-2015.csv")
    # OUTFILE_13_18 = "./data-output/standard-fields/moco-crash-2013-2018.csv"
    # OUTFILE_03_15 = "./data-output/standard-fields/moco-crash-2003-2015.csv"
    DF_13_18 = load_data(sys.argv[1])
    DF_03_15 = load_data(sys.argv[2])
    OUTFILE_13_18 = sys.argv[3]
    OUTFILE_03_15 = sys.argv[4]

    # print(organize_location_cols(rename_df(DF_03_15,rename_dict_03_15)))

    CLEAN_DF_13_18 = rename_df(DF_13_18,rename_dict_13_18)
    CLEAN_DF_03_15 = organize_location_cols(rename_df(DF_03_15,rename_dict_03_15))

    save_clean_df(CLEAN_DF_13_18,OUTFILE_13_18)
    save_clean_df(CLEAN_DF_03_15,OUTFILE_03_15)

    """
    python main_data_cleaning.py "../../source-data/moco-crash-2013-2018.csv" "../../source-data/moco-crash-2003-2015.csv" "../../data-output/temp/moco-crash-2013-2018.csv" "../../data-output/temp/moco-crash-2003-2015.csv"
    """
