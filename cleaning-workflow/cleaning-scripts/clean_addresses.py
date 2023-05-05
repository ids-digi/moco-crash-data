""" 
this script standardizes the addresses of the crash data
input:
    - partially cleaned `csv`s from the `temp` folder
output:
    - `csv`s into the `clean_addresses` folder
"""
import sys

import pandas as pd
import numpy as np
import re


def load_data(crash_file):
    """ returns a pandas dataframe of the raw dataset. """
    return pd.read_csv(crash_file, encoding="unicode_escape")


def replace_str(df, str1, str2):
    """replace string 1 with string 2 in a given df"""
    return df.replace(to_replace=str1, value=str2, regex=True)


# identify strings to manually replace
strs_to_replace = [
    ["BLOOMINGTON IN", ""],
    ["BLOOMINGTON, IN", ""],
    ["S\. ", "S "],
    ["N\. ", "N "],
    ["W\. ", "W "],
    ["E\.", "E"],
    ["SOUTH ", "S "],
    ["NORTH ", "N "],
    ["WEST ", "W "],
    ["EAST ", "E "],
    [" AVE\.", "AVE"],
    ["AVENUE", "AVE"],
    ["STREET", "ST"],
    ["ST\.", "ST"],
    ["PIKE", "PK"],
    ["ROAD", "RD"],
    ["RD RD", "RD"],
    ["STATE RD", "ST RD"],
    ["SR4", "SR 4"],
    ["THIRD", "3RD"],
    [" 47401", ""],
    ["SR ", "ST RD "],
    ["46W", "46 W"],
    ["45W", "45 W"],
    ["STATE 46", "ST RD 46"],
    ["S\.R\.", "ST RD"],
    ["I 69", "I-69"],
    ["I69", "I-69"],
    ["INTERSTATE 69", "I-69"],
    ["I-69 SOUTH", "I-69 S"],
    ["SBOUND", "S"],
    ["S BOUND", "S"],
    ["S I-69", "I-69 S"],
    ["I-69N", "I-69 N"],
    ["JORDAN AVE", "EAGLESON AVE"],
    ["JORDAN", "EAGLESON AVE"],
    ["DRIVE", "DR"],
    ["LANE", "LN"],
    ["IN-45", "ST RD 45"],
    ["W ST RD 45/46 BYPASS", "W ST RD 45/46"],
    ["WMAIN", "W MAIN"],
    ["ROGERS RD", "ROGERS ST"],
    ["BLK ", ""],
    ["N JORDAN", "N EAGLESON AVE"],
    ["S JORDAN", "S EAGLESON AVE"],
    ["E3RD", "E 3RD"],
    ["W3RD", "W 3RD"],
    ["BLOCK ", ""],
    ["STRE", "ST"],
    ["E E", "E "],
    ["3RD AVE", "3RD ST"],
    ["PARKING LOT", ""],
    ["ST ST", "ST"],
    ["2ND AVE", "2ND ST"],
    ["W2ND", "W 2ND"],
    ["E2ND", "E 2ND"],
    ["E10TH", "E 10TH"],
    ["45-46", "45/46"],
    ["SR37", "ST RD 37"],
    ["SR37S", "S ST RD 37"],
    ["OLD SR37", "ST RD 37"],
    ["SR37N", "N ST RD 37"],
    ["OLD ST RD", "ST RD"],
    ["37 BUSINESS", "37"],
    ["37 HWY", "37"],
    ["HWY 37", "ST RD 37"],
    ["OLDSR37", "ST RD 37"],
    ["OLD 37", "ST RD 37"],
    ["ST RD 37S", "S ST RD 37"],
    ["ST RD 37N", "N ST RD 37"],
    ["37 RD", "37"],
    ["ST RD 37 S", "S ST RD 37"],
    ["ST RD 37 N", "N ST RD 37"],
    ["OLST RD 37", "ST RD 37"],
    ["BUSINESS 37", "ST RD 37"],
    ["US37", "ST RD 37"],
    ["ST RD 37 S HWY", "S ST RD 37"],
    ["ST RD 37 N RD", "N ST RD 37"],
    ["DRR", "DRIVER"],
]


def extract_house_nums(road):
    """extract the `101` from `101 E 2ND ST` and create a new column"""
    address_num_exists = False
    if road:
        # get the first word of the road name
        first_word = road.split(" ")[0]
        # get the length of the road name. if there's only one number, we don't want to identify that as an address num.
        road_len = len(road.split(" "))
        if road_len > 1:
            # if the first word is all numerals, the address num exists
            address_num_exists = bool(re.search("^\d+$", first_word))
    # if it exists, return the address num. if not, return an empty string.
    return first_word if address_num_exists else ""


def remove_house_nums(road):
    """All entries like `101 E 2ND ST` should be `E 2ND ST`"""
    address_num_exists = False
    if road:
        first_word = road.split(" ")[0]
        road_len = len(road.split(" "))
        if road_len > 1:
            address_num_exists = bool(re.search("^\d+$", first_word))
    #         if the address num exists, remove it from the original address. else, return original address.
    return " ".join(road.split(" ")[1:]) if address_num_exists else road


def clean_numbered_streets(road):
    """All entries like `S 17TH` should be `S 17TH ST`"""
    if road:
        if bool(re.search("[\d]{1,2}(TH|ST|ND|RD)$", road.strip())):
            road = road.strip() + " ST"
    return road.strip()


def remove_colons(road):
    """remove info after semicolons or colons"""
    if road:
        road = road.split(";")[0]
        road = road.split(":")[0]
    return road


def clean_addresses(df):
    df["Roadway Id"] = df["Roadway Id"].fillna("")
    for string in strs_to_replace:
        df = replace_str(df, string[0], string[1])
    df["Address Number"] = df["Roadway Id"].apply(extract_house_nums)
    df["Roadway Id"] = df["Roadway Id"].apply(remove_house_nums)
    df["Roadway Id"] = df["Roadway Id"].apply(remove_colons)
    df["Primary Factor"] = df["Primary Factor"]
    return df


def save_clean_df(cleaned_df, out_file):
    """ save the cleaned df """
    cleaned_df.to_csv(out_file, index=False)


if __name__ == "__main__":

    DF = load_data(sys.argv[1])
    OUTFILE = sys.argv[2]

    CLEAN_DF = clean_addresses(DF)
    save_clean_df(CLEAN_DF, OUTFILE)

    print("addresses have been cleaned for", sys.argv[1])
