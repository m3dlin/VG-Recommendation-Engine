"""
this module is used to collect data from the steamspy api
by using app ids and adding to a csv. Must use in separate batches
because there was too many api calls at one time.
"""

# standard libraries
import time

# secondary libraries
from pandas.io.json import json_normalize
import pandas as pd
import requests


# used to request info from api and collect json
def get_request(url, parameters):
    response = requests.get(url=url, params=parameters)
    if response:
        return response.json()
    else:
        # too many requests. Wait and try again
        print('No response, waiting 10 seconds...')
        time.sleep(10)
        print('Retrying.')
        return get_request(url, parameters)


# used to get game ids per page and return a list of all ids found
def get_game_ids(page):
    url = "https://steamspy.com/api.php?request=all&page="
    temp_url = url
    temp_url += str(page)
    parameters = {"request": "all"}
    json_data = get_request(temp_url, parameters)
    df = pd.DataFrame.from_dict(json_data, orient='index')
    print("page " + str(page) + " processed")
    id_list = df["appid"].reset_index(drop=True)
    print("done with retrieving ids")
    return id_list


# using the app id, get info on that specific game
def get_game_info(app):
    url = "https://steamspy.com/api.php"
    parameters = {"request": "appdetails", "appid": app}
    json_data = get_request(url, parameters)
    df = pd.DataFrame.from_dict(json_data, orient='index').transpose()
    return df


if __name__ == "__main__":
    url = "https://steamspy.com/api.php"

    # collecting pages of app ids individually
    # list_of_appids = get_game_ids(0)
    # list_of_appids = get_game_ids(1)
    # list_of_appids = get_game_ids(2)
    # list_of_appids = get_game_ids(3)
    list_of_appids = get_game_ids(4)

    # page
    frames = []
    for app in list_of_appids:
        frames.append(get_game_info(app))
        print("loaded " + str(app))
        time.sleep(1)
    steam_spy_data = pd.concat(frames)
    games_list = steam_spy_data.reset_index(drop=True)
    # adding pages of games to individual csv files. Will be combined into one
    # games_list.to_csv("steam_spy_games_list_page_0.csv")
    # games_list.to_csv("steam_spy_games_list_page_1.csv")
    # games_list.to_csv("steam_spy_games_list_page_2.csv")
    # games_list.to_csv("steam_spy_games_list_page_3.csv")
    games_list.to_csv("steam_spy_games_list_page_4.csv")

    print("data was saved to a csv")
