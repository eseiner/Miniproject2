import pandas as pd

def get_most_popular():
    data = pd.read_csv('data/data.csv')
    top_ten = data.value_counts(subset=['Movie ID'])
    ids = []
    for element in list(top_ten.keys()):
        ids.append(element[0])
    return ids

def get_highest_rated():
    data = pd.read_csv('data/data.csv')
    id_rating = data[['Movie ID', 'Rating']]
    avg_ratings = id_rating.groupby(['Movie ID'], as_index=False).mean()
    avg_ratings = avg_ratings.sort_values(by=['Rating'], ascending=False)
    ids = list(avg_ratings['Movie ID'])
    return ids

def get_choice_of_movies():
    # Id's of selected movies
    ids = [1127, 318, 196, 405, 173, 1484, 1219, 902, 820, 780]
    return ids

def get_comedy_movies():
    ids = [1, 25, 41, 67, 70, 91, 94, 138, 154, 163]
    return ids

def get_musical_movies():
    ids = [21, 71, 95, 99, 143, 418, 419, 451, 543, 1459]
    return ids

def get_scifi_movies():
    ids = [50, 62, 82, 89, 96, 121, 135, 141, 172, 181]
    return ids