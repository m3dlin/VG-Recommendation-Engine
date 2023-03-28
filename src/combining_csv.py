"""
this module is used to combine all 5 csv's
into one "master" csv
"""
import pandas as pd

# read csv files into dataframes
list0 = pd.read_csv("steam_spy_games_list_page_0.csv")
list1 = pd.read_csv("steam_spy_games_list_page_1.csv")
list2 = pd.read_csv("steam_spy_games_list_page_2.csv")
list3 = pd.read_csv("steam_spy_games_list_page_3.csv")
list4 = pd.read_csv("steam_spy_games_list_page_4.csv")

frames = [list0, list1, list2, list3, list4]

# combining all frames into one and putting it to a csv
official_list = pd.concat(frames, ignore_index=True)
official_list.to_csv("official_steam_games_list.csv")
