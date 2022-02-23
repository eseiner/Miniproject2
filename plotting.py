import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from helper import get_plotting_kwargs
import seaborn as sns;



def plot(V_tilde, idx, title):
    ''' Takes in indicies of movies to annotate and plots'''
    movies_data = pd.read_csv('data/movies.csv')
    ID_column = 'Movie ID'
    title_column = 'Movie Title'
    avg_ratings, num_ratings = get_plotting_kwargs()
    plt.figure(figsize=(15, 12))
    sns.set()
    ax = sns.scatterplot(V_tilde[0], V_tilde[1], hue=avg_ratings, size=num_ratings, palette='rocket_r')
    sm = plt.cm.ScalarMappable(cmap='rocket_r')
    sm.set_array([1, 5])
    # Remove the legend and add a colorbar
    ax.get_legend().remove()
    ax.figure.colorbar(sm)
    for movie in movies_data[ID_column].values[idx]:
        movie_id = movie - 1
        movie_title = movies_data[title_column].iloc[movie_id]
        label_x, label_y = V_tilde[0][movie_id], V_tilde[1][movie_id]
        plt.annotate(movie_title, xy=(label_x, label_y), horizontalalignment='center', verticalalignment='center', color='black', fontsize=12, alpha=0.7)
