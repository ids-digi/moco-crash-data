"""
this script updates the geocoding for all crash reports with two roads listed,
which enables intersection geocoding.

IMPORTANT: this code will take a long time to run, around an hour for each 
of the small data sets. It took more than 16 hours to run on the master file. 

If you don't want to spend the time, you can use the already geocoded data in the 
data/clean-data/geocoded file or the data/clean-data/jittered file
"""

import sys

# pandas
import pandas as pd

# regex
import re

# geopy for geolocation
import geopy
from geopy.geocoders import ArcGIS
from geopy.extra.rate_limiter import RateLimiter

# progress bar
from tqdm import tqdm

tqdm.pandas()


def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset """
    return pd.read_csv(in_file, low_memory=False)


# define a function to geolocate a given column
def geocode_intersection(road1, road2):
    if len(str(road2)) > 0:
        print(road1, road2)
        n = ArcGIS().geocode(road1 + " & " + road2 + ", BLOOMINGTON IN")
        # n is a list [0] = street names [1] = lat/long
        return n[1]
    else:
        return ""


def apply_geocode(df):
    df["new_coords"] = df.progress_apply(
        lambda x: geocode_intersection(x["Roadway Id"], x["Intersecting Road"]), axis=1
    )
    return df


def split_coords(string, index):
    test = re.findall("[\d]{2}\.[\d]{5}", str(string))
    return float(test[index]) if len(test) > 1 else ""


def clean_geocode_coords(df):
    df["Latitude_2"] = df["new_coords"].apply(lambda x: x["Roadway Id"], 0, axis=1)
    df["Longitude_2"].apply(lambda x: x["Roadway Id"], 1, axis=1)
    return df


def merge_lat_lon(coord1, coord2):
    if coord2 == "":
        return coord1
    else:
        return coord2


def apply_merge(df):
    df["Latitude"] = df.apply(
        lambda x: merge_lat_lon(x["Latitude"], x["Latitude_2"]), axis=1
    )
    df["Longitude"] = df.apply(
        lambda x: merge_lat_lon(x["Longitude"], x["Longitude_2"]), axis=1
    )
    return df


def save_clean_df(cleaned_df, out_file):
    """ save the master df """
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":
    DF = load_data(sys.argv[1])
    OUTFILE = sys.argv[2]

    CLEAN_DF = apply_merge(clean_geocode_coords(apply_geocode(DF)))

    save_clean_df(CLEAN_DF.drop(columns=["Latitude_2", "Longitude_2", "new_coords"]))

    print("geocode updated successfully for", DF)
