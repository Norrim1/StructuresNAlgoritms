from matplotlib import pyplot as plt
import numpy
import pandas as pd


games = pd.read_csv('vgsales.csv')
metacritic = pd.read_csv("metacritic_games.csv")

print(games['Platform'].unique())
games_copy = games.copy()

games_copy = games_copy.merge(
    right=metacritic[['name', 'rating']],
    how='left',
    left_on='Name',
    right_on='name'
)

print(games_copy)

games_m = games_copy[(games_copy['rating'] == 'M') & (games_copy['Year'] >= 2012)]
print(games_m)