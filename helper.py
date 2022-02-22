from csv import unregister_dialect
import pandas as pd
import numpy as np

def get_most_popular():
    data = pd.read_csv('data/data.csv')
    top_ten = data.value_counts(subset=['Movie ID'])
    ids = []
    for element in list(top_ten.keys()):
        ids.append(element[0]-1)
    return ids

def get_highest_rated():
    data = pd.read_csv('data/data.csv')
    id_rating = data[['Movie ID', 'Rating']]
    avg_ratings = id_rating.groupby(['Movie ID'], as_index=False).mean()
    avg_ratings = avg_ratings.sort_values(by=['Rating'], ascending=False)
    ids = list(avg_ratings['Movie ID'])
    ids = list(np.array(ids)-1)
    return ids

def get_plotting_kwargs():
    data = pd.read_csv('data/data.csv')
    data = data.to_numpy()
    N = max(data[:,1]).astype(int)
    num_ratings = np.zeros(N)
    tot_ratings = np.zeros(N)
    for movie in data:
        movie_id = movie[1]-1
        rating = movie[2]
        num_ratings[movie_id] += 1
        tot_ratings[movie_id] += rating
    avg_ratings = tot_ratings / num_ratings
    return (avg_ratings, num_ratings)
