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