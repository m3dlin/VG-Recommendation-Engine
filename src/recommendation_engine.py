"""
this module contains functions used for the gui.
the main purpose of this module is to collect recommendations when given a valid game input.
this is also where the recommendations and their information will be formatted to display
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# recommendation engine has access to the new data
import data_cleaning as dc

data = dc.revised_data

# need to change the keyword column to strings in order to use Count Vectorizer
for i in range(len(data)):
    row = data.loc[i, 'combined keywords']
    data.loc[i, 'combined keywords'] = ' '.join(row)
    # change names to lowercase
    row = data.loc[i, 'name']
    data.loc[i, 'name'] = row.lower()

# CountVectorizer: used to transform string of text into token counts
# it will count how many times keywords are used and compare it to the other strings
cv = CountVectorizer()
count_matrix = cv.fit_transform(data['combined keywords'])

# this shows off the matrix, similarity score is from 0 to 1 (1 being exactly alike, 0 being not at all alike)
# print(count_matrix.toarray())
cs = cosine_similarity(count_matrix)


# function used in the GUI to find which row/index the game is at
def find_game_index(name):
    new_name = name.lower()
    return int(data[data['name'] == new_name].index.to_numpy())


# returns 4 lists, each one is a different property of each game
def get_games(index):
    # list of the matrix, enumerate keeps track of which indexes are chosen
    similar_games = list(enumerate(cs[index]))

    # putting games in sorted order from most similar to least
    games_list = sorted(similar_games, key=lambda x: x[1], reverse=True)

    # list of all individual properties that will be displayed to user
    name_list = []
    price_list = []
    rating_list = []
    link_list = []
    i = 0
    for game in games_list:
        name_list.append(data.loc[game[0], 'name'])
        price_list.append((data.loc[game[0], 'price']) / 100)
        rating_list.append((data.loc[game[0], 'rating_score']) * 100)
        link_list.append('https://store.steampowered.com/app/' + str(data.loc[game[0], 'appid']))
        i = i + 1
        if i > 10:
            break
    return [name_list, price_list, rating_list, link_list]


# main function used for gui to display recommendations
def get_recommendations(index):
    # test_game contains all the lists for each property
    test_game = get_games(index)
    name_list = test_game[0]
    price_list = test_game[1]
    rating_list = test_game[2]
    link_list = test_game[3]

    # list contains each string per game
    data_list = []

    """
    format:
    stardew valley      price: 00.00        rating: 00%     link: https://store.steampowered.com/app/000

    """
    for i in range(11):
        # I do not want to display the first game (the original game)
        if i == 0:
            continue
        data_list.append(name_list[i].ljust(40) + 'price: $' + str(price_list[i]).ljust(10)
                         + 'rating: ' + str(int(rating_list[i])) + "%".ljust(5) + 'store link: ' + link_list[i])

    return data_list


# ensuring that the game the user enters in GUI is part of the games list
def validate_name(name):
    name = name.lower()
    for i in range(len(data)):
        if name == data.loc[i, 'name']:
            return True
    return False


# used to collect list of appids for GUI to display correct appid for the URL
def list_of_appids(index):
    similar_games = list(enumerate(cs[index]))
    # putting games in sorted order from most similar to least
    games_list = sorted(similar_games, key=lambda x: x[1], reverse=True)
    i = 0
    appid_list = []
    for game in games_list:
        if i == 0:
            i = i + 1
            continue
        appid_list.append(str(data.loc[game[0], 'appid']))  # must be string for display format
        i = i + 1
        if i > 10:
            break

    return appid_list
