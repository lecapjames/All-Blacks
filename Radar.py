import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# This code asks the user for an input and produces a radar plot for a player. The
# plot is based on the player's performance percentiles in each statistical category.
# Comment out the necessary lines to run two plots at once.

# Load your dataset into a DataFrame
df_80 = pd.read_csv('C:/Users/olive/Documents/All Black Project/Per_80_Minute_Avg.csv')
df_advanced = pd.read_csv('C:/Users/olive/Documents/All Black Project/Advanced_Statistics.csv')

df = df_80.merge(df_advanced, on='Name')

# Get Player Input
player_name1 = input("Enter first player name: ")
#player_name2 = input("Enter second player name: ")

graph_type = input('Enter "P" for positive stats, "N" for negative stats or'
                   '"A" for advanced stats: ')

# Select related columns for each graph type
if graph_type == "P":
    data_columns = ['Tries', 'Try Assists', 'Try Contributions', 'Carries',
                'Meters', 'Defenders Beaten', 'Linebreaks',
                'Offloads', 'Tackles', 'Tackle %', 'Turnovers Won']
    description = "Positive Performance Percentiles"
elif graph_type == "N":
    data_columns = ['Missed Tackles',
            'Turnovers Lost', 'Penalties']
    description = "Negative Performance Percentiles"
elif graph_type == "A":
    data_columns = ['Player Rating', 'Carry Rating', 'Offensive Rating', 'Defensive Rating', 'Tackle Rating']
    description = "Advanced Performance Percentiles"

def radar_plotter(player_name):

    # Get Player Data
    player_data = df[df['Name'] == player_name]

    # Calculate percentiles
    percentiles = [df[cat].rank(pct=True).iloc[player_data.index[0]] * 100 for cat in data_columns]

    # Make figure

    fig = px.line_polar(percentiles, r=percentiles, theta=data_columns, line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'{player_name} {description}')
    fig.show()

radar_plotter(player_name1)
#radar_plotter(player_name2)

