import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from helper import get_plotting_kwargs



def plot(V_proj, idx, title):
    ''' Takes in indicies of movies to annotate and plots'''
    movies = pd.read_csv('data/movies.csv')
    avg_ratings, num_ratings = get_plotting_kwargs()
    plt.figure(figsize=(15, 12))
    plt.scatter(V_proj[0], V_proj[1], s=num_ratings, c=avg_ratings, cmap=plt.get_cmap('RdYlGn'), alpha=0.6)
    plt.colorbar().set_label("Average rating")
    plt.title(title)
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    for movie_id, title in movies[['Movie ID', 'Movie Title']].values[idx]:
        x, y = V_proj[0][movie_id-1], V_proj[1][movie_id-1]
        plt.annotate(title, xy=(x, y), horizontalalignment='center', verticalalignment='center', fontsize=8, rotation=0, arrowprops=dict(arrowstyle='-', lw=1, alpha=0.5))
    plt.show()