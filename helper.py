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
    ids = list(np.array(avg_ratings['Movie ID'])-1)
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


def get_choice_of_movies():
    # Id's of selected movies
    ids = [1127, 318, 196, 405, 173, 1484, 1219, 902, 820, 780]
    for i in range(len(ids)):
        ids[i] = ids[i] - 1
    return ids

def get_comedy_movies():
    ids = [1, 25, 41, 67, 70, 91, 94, 138, 154, 163]
    for i in range(len(ids)):
        ids[i] = ids[i] - 1
    return ids

def get_musical_movies():
    ids = [21, 71, 95, 99, 143, 418, 419, 451, 543, 1459]
    for i in range(len(ids)):
        ids[i] = ids[i] - 1
    return ids

def get_scifi_movies():
    ids = [50, 62, 82, 89, 96, 121, 135, 141, 172, 181]
    for i in range(len(ids)):
        ids[i] = ids[i] - 1
    return ids

def mean_center_rows(V):
    # "hello"
    V_mean_ctr = np.zeros_like(V)
    for row_num in range(V.shape[0]):
        curr_mean = sum(V[row_num]) / V.shape[1]
        # subtract curr_mean from every element in the row
        V_mean_ctr[row_num] = V[row_num] - curr_mean
    return V_mean_ctr
