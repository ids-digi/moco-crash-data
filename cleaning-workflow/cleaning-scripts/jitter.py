"""
this script uses the cleaned, geocoded csv in the data/clean-data/geocoded file
to add geocoded lat/lon to the master.csv file and then jitter the points. 

jittering the points, meaning shifting them slightly will, make it easier to 
see individual crashes that all occurred at the same place on a map.

the geocoded master file was produced by running the geocode.py script on the 
master.csv file output, which took a very long time.

input: 
- data/clean-data/master-crashes.csv
- data/clean-data/geocoded/master_crash_geocoded.csv
output: 
- data/clean-data/master-crashes.csv
- data/clean-data/jittered/master-crashes-jittered/csv
"""

import sys
import pandas as pd
import random


def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset """
    return pd.read_csv(in_file, low_memory=False)


def merge_geocoded_lat_lon(master, geocoded_master):
    geocoded = master.merge(geocoded_master, how="left", on="DateTime")
    master["Latitude"] = geocoded["Latitude_y"]
    master["Longitude"] = geocoded["Longitude_y"]
    return master


def find_duplicates(df):
    df["duplicate?"] = df.duplicated(
        subset=[("Roadway Id" and "Intersecting Road") or ("Latitude" and "Longitude")]
    )
    return df


# define a function to return a jittered coordinate based on the original coordinate
def jitter(coord):
    jitter_val = random.random() * (0.0001 - 0.00005) - 0.00005
    return coord + jitter_val


def add_jitter(df):
    df.loc[df["duplicate?"] == True, "Latitude"] = df["Latitude"].apply(jitter)
    df.loc[df["duplicate?"] == True, "Longitude"] = df["Longitude"].apply(jitter)
    return df.drop(columns="duplicate?")


def save_clean_df(cleaned_df, out_file):
    """ save the df """
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":
    DF = load_data(sys.argv[1])
    GEOCODED_DF = load_data(sys.argv[2])
    OUTFILE = sys.argv[3]

    JITTERED_DF = add_jitter(find_duplicates(merge_geocoded_lat_lon(DF, GEOCODED_DF)))

    save_clean_df(JITTERED_DF, OUTFILE)

    print(sys.argv[1], "jittered successfully")
