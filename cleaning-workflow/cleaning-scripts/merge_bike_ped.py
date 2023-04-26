""" 
this script adds bike and ped columns to the data from 2013-2018
the source data for the bike/ped crashes is from the city
"""
import sys
import os

import pandas as pd


def load_data(file):
    """ returns a pandas dataframe of a csv. """
    return pd.read_csv(file, encoding="unicode_escape")


def merge(main_df, df_to_merge, new_col_name):
    """merges the bike or ped data wtih the original csv"""
    dates = df_to_merge["DateTime"].reset_index()
    dates[new_col_name] = True
    return main_df.merge(dates, how="left", on="DateTime")


def save_merged_df(merged_df, out_file):
    """ save the merged df """
    merged_df.drop(columns=["index_x", "index_y"]).to_csv(out_file, index=False)


def remove_temp_file(file):
    """remove temp file from folder since the files will be fully cleaned after this script runs"""
    print(file)
    os.remove(file)


if __name__ == "__main__":

    DF = load_data(sys.argv[1])
    BIKE_DF = load_data(sys.argv[2])
    PED_DF = load_data(sys.argv[3])
    OUTFILE = sys.argv[4]

    MERGED_DF = merge(DF, BIKE_DF, "Cyclist Involved")
    MERGED_DF = merge(MERGED_DF, PED_DF, "Pedestrian Involved")
    save_merged_df(MERGED_DF, OUTFILE)

    remove_temp_file(sys.argv[1])

    print("bike/ped data has been added to", sys.argv[4])

    """
    python merge_bike_ped.py "main-file" "bike-file" "ped-file" "output-file" 
    """
