import pandas as pd

# Read in a Spreadsheet with the total stats for each player.
df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Stat_Totals.csv')

# Define columns containing numerical values
data_cols = [
    "Minutes", "Tries", "Try Assists", "Try Contributions", "Carries", "Meters",
    "Defenders Beaten", "Linebreaks", "Offloads", "Tackles", "Missed Tackles",
    "Turnovers Won", "Turnovers Lost", "Penalties", "Kicks", "Passes",
    "Dominant Tackles"
]

# Calculate per game averages
per_game_df = df.copy()
per_80_df = df.copy()

# Calculate both per game and per 80 minute adjusted averages
for column in data_cols:
    per_game_df[column] = df[column] / df['Games Played']
    per_80_df[column] = (df[column] / df['Minutes']) * 80

per_game_df.to_csv('C:/Users/olive/Documents/All Black Project/Per_Game_Avg.csv')
per_80_df.to_csv('C:/Users/olive/Documents/All Black Project/Per_80_Minute_Avg.csv')
