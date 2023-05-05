"""
this script produces a master file, useful for mapping or comparing
general crash statistics across all years. 

the master file will have fewer columns, because most columns are not 
comparable across all years of data. it also estimates the deaths and 
injuries for years 2003-2012. 

in the source data, there is overlap for years 2013-2015. this script
will drop years 2013-2015 from the `moco-crash-2003-2015.csv` file in 
the interest of keeping the more accurate death/injury counts noted
in the newer data file. but the `moco-crash-2003-2015.csv` file does
include more specific pedestrian/cyclist involvement data, which is
not included in this master file. 

data after 2012 has exact counts for each crash for deaths and injuries.
data before 2013 only has a true/false value to indicate death or injury.
therefore, this script will convert all `true` values to 1 death or 
injury, and all false values to 0, to provide a low estimate that is
more comparable and easier to map. 

analysis of 2003-2012 should NOT rely on the death/injury numbers from this
master dataset as exact numbers. instead, more specific analysis should
be based on the specific 2003-2015 file, not the master file.
"""

import sys

import pandas as pd


def load_data(in_file):
    """ returns a pandas dataframe of the raw dataset """
    return pd.read_csv(in_file, low_memory=False)


def drop_cols(df):
    """ drops uncomparable or unuseful columns. keeps cols useful for mapping """
    cols_to_drop = [
        "Collision Date",
        "Collision Time",
        "House Number",
        "Roadway Interchange",
        "Roadway Ramp",
        "Interchange",
        "Feet From",
        "Direction",
        "Construction Type",
        "Type of Median",
        "_id",
        "Traffic Control",
        "_id",
        "Agency",
        "City",
        "Trailers Involved",
        "Number Deer",
        "Roadway Class",
        "Hit and Run?",
        "Locality",
        "School Zone?",
        "Rumble Strips?",
        "Construction?",
        "Roadway Junction Type",
        "Road Character",
        "Roadway Surface",
        "Ramp",
        "Property Type",
        "Dir",
        "Road Class",
        "H&R",
        "School ",
        "Light",
        "Median",
        "Rumble Strips",
        "Master Record Number",
        "CN Type",
        "Unique Location Id",
        "Light Condition",
        "Weather Conditions",
        "Surface Condition",
        "Local Code",
        "County",
        "Township",
        "Roadway Suffix",
        "Roadway Name",
        "Roadway Number",
        "Intersecting Road Number",
        "Mile Marker",
        "Corporate Limits",
        "Traffic Control Devices?",
        "Aggressive Driving?",
        "Damage Estimate",
        "State Property Damage?",
        "Corporate Limits?",
    ]
    return df.drop(cols_to_drop, axis=1, errors="ignore")


def get_year(date):
    return pd.to_datetime(date).year


def drop_duplicate_years(df):
    df["Year"] = df["DateTime"].apply(get_year)
    return df[df["Year"] < 2013].drop(columns=["Year"])


def injury_estimate(string):
    if string == "Non-incapacitating":
        return 1
    elif string == "Incapacitating":
        return 1
    else:
        return 0


def fatality_estimate(string):
    if string == "Fatal":
        return 1
    else:
        return 0


def num_vehicle_estimate(string):
    if string == "1-Car":
        return 1
    elif string == "2-Car":
        return 2
    elif string == "3+ Cars":
        return 3
    else:
        return 0


def estimate_fields(df):
    df["Number Dead"] = df["Injury Type"].apply(fatality_estimate)
    df["Number Injured"] = df["Injury Type"].apply(injury_estimate)
    df["Vehicles Involved"] = df["Vehicles Involved"].apply(num_vehicle_estimate)
    return df.drop(columns=["Injury Type", "Vehicles Involved"])


def combine_dfs(df_list):
    return pd.concat(df_list)


def save_clean_df(cleaned_df, out_file):
    """ save the master df """
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":
    DFS = sys.argv[1:-1]
    OUTFILE = sys.argv[-1]

    CLEAN_DFS = list(map(load_data, DFS))

    for i, df in enumerate(CLEAN_DFS):
        """if it's the 2003-2015 data, drop duplicate years and add death/injury estimates"""
        if "2011-03-06 18:00:00" in set(df["DateTime"]):
            CLEAN_DFS[i] = estimate_fields(drop_duplicate_years(df))

    CLEAN_DFS = list(map(drop_cols, CLEAN_DFS))

    master = combine_dfs(CLEAN_DFS)

    save_clean_df(master, OUTFILE)

    print("master file saved successfully")
