# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:28:34 2023

@author: ericj
"""

# import data
import numpy as np
import pandas as pd

from pandas import DataFrame
from numpy import random


address_gamedets = r"C:\Users\ericj\OneDrive\Documents\GitHub\NBA\games_details.csv"
address_game = r'C:\Users\ericj\OneDrive\Documents\GitHub\NBA\games.csv'
address_players = r'C:\Users\ericj\OneDrive\Documents\GitHub\NBA\players.csv'
address_ranking = r'C:\Users\ericj\OneDrive\Documents\GitHub\NBA\ranking.csv'
address_teams = r'C:\Users\ericj\OneDrive\Documents\GitHub\NBA\teams.csv'


game_details = pd.read_csv(address_gamedets)
game = pd.read_csv(address_game)
players = pd.read_csv(address_players)
ranking = pd.read_csv(address_ranking)
teams = pd.read_csv(address_teams)

# look at data

game_details.head()
game.head()
players.head()
ranking.head()
teams.head()

teams.info()
game.info()
players.info()

teams

players['TEAM_ID'].value_counts()
players.TEAM_ID.value_counts()

# summarizing data for median
players.groupby('SEASON').median()

# check unique seasons
np.unique(game['SEASON'])

list(players)

players.shape

players.describe()

players.info()

players[(players['PLAYER_NAME']=='Mike Conley')&(players['TEAM_ID']==1610612762)].head()

players.query(PLAYER_NAME='Mike Conley')

# look at column header
game.columns

game.dtypes


game.info()
game_details.info()

game.count()
game.SEASON.count()
game.GAME_ID.count()
game['SEASON'].count()
game[['SEASON','GAME_ID']].count()

game.SEASON.value_counts()
game.SEASON.unique()
game.SEASON.nunique()

game.HOME_TEAM_WINS.mean()

game.head()

game.describe()


game.groupby('SEASON')['PTS_home'].sum()
plt.plot(game.groupby('SEASON')['PTS_home'].sum())

game.groupby(['SEASON','HOME_TEAM_WINS'])['PTS_home'].sum()

game.groupby(['SEASON'])[['PTS_home','PTS_away']].sum()
game.groupby(['SEASON','HOME_TEAM_WINS'])[['PTS_home','PTS_away']].sum()


game.groupby(['SEASON','HOME_TEAM_WINS']).agg(
    maxpts = ('PTS_home','max'),
    minpts = ('PTS_home','min'),
    avgpts = ('PTS_home','mean'),
    medpts = ('PTS_home','median'),
    gappts = ('PTS_home', lambda x: (max(x)-min(x)))
    )

# join tables
pd.merge(game_details,game,on="GAME_ID").head()


