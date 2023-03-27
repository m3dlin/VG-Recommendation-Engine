# NOTE: to show link to games https://store.steampowered.com/app/2540 (last digits are the appid)
import pandas as pd

data = pd.read_csv('official_steam_games_list.csv')
print(data.head())