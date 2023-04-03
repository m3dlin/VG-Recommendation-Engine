"""
this module is used to identify what data is
necessary for the recommendation engine
"""


import pandas as pd
import re
import json

data = pd.read_csv('official_steam_games_list.csv')


# remove columns that are not needed for the engine
def remove_nonessential_cols():
    new_data = data.drop(
        columns=['publisher', 'userscore', 'owners', 'average_forever', 'owners', 'average_2weeks',
                 'median_forever', 'median_2weeks', 'discount', 'initialprice', 'ccu'])
    return new_data


# rating is from 0-1, the closer to 1 the rating is the better
def calculating_rating(df):
    ratings = []
    for i in range(len(df)):
        total_positive = df.loc[i, 'positive']
        total_negative = df.loc[i, 'negative']
        if total_negative + total_positive != 0:
            rating = total_positive / (total_negative + total_positive)
            ratings.append(rating)
        else:
            ratings.append(0)
    df.insert(9, "rating_score", ratings, True)
    return df


# makes sure that each game has a legit name and there's no random characters for an invalid name
def contains_random_chars(df):
    # ensures that a title has 3 valid characters in succession
    pattern = re.compile('[^\u0001-\u007F]{3,}')

    # create a boolean mask to indicate which rows are bad
    mask = df['name'].str.contains(pattern)
    # remove rows with invalid title names
    df = df[~mask]

    return df


# taking all the tags and putting it into an array for each row
# this array will be added to a new dataframe column
def collecting_tags_col(df):
    list_of_tags = []  # collects arrays

    for i in range(len(df)):
        text = df.loc[i, 'tags']
        text = text.replace("'", '"')  # correct json format
        json_object = json.loads(text)
        tags_per_row = []  # array of tags
        # if the game does not have any tags, then its array is empty and skips it
        if not bool(json_object):
            list_of_tags.append([])
            continue
        # key is referring to the json key, I only need the name not the number
        for key in json_object.keys():
            tags_per_row.append(key)
        list_of_tags.append(tags_per_row)  # this array collecting each row array

    df.insert(10, "list of tags", list_of_tags, True)  # new column
    return df


revised_data = remove_nonessential_cols()
revised_data = calculating_rating(revised_data)

# for each row, ensure that the json is in the correct format
for i in range(len(revised_data)):
    data = revised_data.loc[i, 'tags']
    json_str = data.replace("Beat 'em up", "Beat em up")  # take off '
    json_str = json_str.replace("Shoot 'Em Up", "Shoot Em Up")  # take off '
    json_str = re.sub(r'(?<!1990)\'', '"', json_str)  # replacing all ' with " except for 1990's
    json_str = json_str.replace("1990's", "1990s")  # take off '
    revised_data.at[i, 'tags'] = json_str  # put new json format into dataframe

revised_data = collecting_tags_col(revised_data)
