"""
this module is used to identify what data is
necessary for the recommendation engine
"""

# NOTE: to show link to games https://store.steampowered.com/app/2540 (last digits are the appid)
import pandas as pd

data = pd.read_csv('official_steam_games_list.csv')


def remove_nonessential_cols():
    new_data = data.drop(
        columns=['publisher', 'userscore', 'owners', 'average_forever', 'owners', 'average_2weeks',
                 'median_forever', 'median_2weeks', 'discount', 'initialprice', 'ccu'])
    return new_data


def calculating_rating(data):
    ratings = []
    for i in range(len(data)):
        total_positive = data.loc[i, 'positive']
        total_negative = data.loc[i, 'negative']
        if total_negative + total_positive != 0:
            rating = total_positive / (total_negative + total_positive)
            ratings.append(rating)
        else:
            ratings.append(0)
    data.insert(9, "rating_score", ratings, True)
    return data


revised_data = remove_nonessential_cols()
calculating_rating(revised_data)


