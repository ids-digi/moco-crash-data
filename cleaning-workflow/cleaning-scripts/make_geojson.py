"""
this script creates the final geojson used for mapping
it outputs three geojsons: 
1. fatal crashes only
2. crashes resulting in injury only
3. crashes that didn't result in fatalities or injuries
"""

import sys

import pandas as pd

from pandas_geojson import to_geojson
from pandas_geojson import write_geojson


def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset """
    return pd.read_csv(in_file, low_memory=False)


def drop_out_of_bounds_points(map_df):
    return map_df[
        (map_df["Latitude"] > 38.99133)
        & (map_df["Latitude"] < 39.35543165)
        & (map_df["Longitude"] < -86.32442)
        & (map_df["Longitude"] > -86.68285)
    ]


def minimize_field_names(df):
    rename_dict = {
        "Vehicles Involved": "v",
        "Number Injured": "i",
        "Number Dead": "d",
        "Roadway Id": "r",
        "Intersecting Road": "r2",
        "Primary Factor": "f",
        "Manner of Collision": "m",
        "DateTime": "dt",
        "Cyclist Involved": "c",
        "Pedestrian Involved": "p",
    }
    return df.rename(rename_dict)


def round_digits(coord):
    return round(coord, 6)


def round_lat_lon(df):
    df[["Latitude", "Longitude"]] = df[["Latitude", "Longitude"]].apply(round_digits)
    return df


def save_deaths(df, outfile):
    deaths = df["d" > 0]
    death_geo_json = to_geojson(
        df=df[deaths].fillna(""),
        lat="Latitude",
        lon="Longitude",
        properties=["i", "d", "v", "r", "r2", "f", "m", "dt", "c", "p"],
    )
    write_geojson(death_geo_json, filename=outfile)


def save_injuries(df, outfile):
    deaths = df["d" > 0]
    injuries = df["i" > 0]
    injuries_geojson = to_geojson(
        df=df[~deaths][injuries].fillna(""),
        lat="Latitude",
        lon="Longitude",
        # remove the "d" death category bc there are no deaths in this df
        properties=["i", "v", "r", "r2", "f", "m", "dt", "c", "p"],
    )
    write_geojson(injuries_geojson, filename=outfile)


def save_nonfatal(df, outfile):
    deaths = df["d" > 0]
    injuries = df["i" > 0]
    nonfatal_geojson = to_geojson(
        df=df[~deaths][~injuries].fillna(""),
        lat="Latitude",
        lon="Longitude",
        # remove the "d" death and "i" injuries categories bc
        # this df only includes rows w/o these fields
        properties=["v", "r", "r2", "f", "m", "dt", "c", "p"],
    )
    write_geojson(nonfatal_geojson, filename=outfile)


if __name__ == "__main__":
    DF = load_data(sys.argv[1])
    OUTFILE_DEATHS = sys.argv[2]
    OUTFILE_INJURIES = sys.argv[3]
    OUTFILE_NONFATAL = sys.argv[4]

    MIN_DF = minimize_field_names(round_lat_lon(drop_out_of_bounds_points(DF)))

    save_deaths(MIN_DF, OUTFILE_DEATHS)
    save_injuries(MIN_DF, OUTFILE_INJURIES)
    save_nonfatal(MIN_DF, OUTFILE_NONFATAL)

    print("geojson saved successfully")
