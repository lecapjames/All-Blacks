import pandas as pd

# Code reads in the collated dataset and totals each stat for all players
# in the dataset. It also adds a 'Games Played' column to the output csv.

# Read in the complete collated dataset.
df = pd.read_csv('C:/Users/olive/Documents/All Black Project/ALLBLACKDATA.csv')

# Add a new Games Played column
df['Games Played'] = 1

# Define columns containing numerical values
data_cols = [
    "Minutes", "Tries", "Try Assists", "Try Contributions", "Carries", "Meters",
    "Defenders Beaten", "Linebreaks", "Offloads", "Tackles", "Missed Tackles",
    "Turnovers Won", "Turnovers Lost", "Penalties", "Kicks", "Passes",
    "Dominant Tackles", "Games Played"
]

# Groups by player name and retains their position
position_grouped = df.groupby('Name')['Position'].first()

# Groups by player name and data columns
data_grouped = df.groupby('Name')[data_cols].sum()

# Merge the data
merged_data = data_grouped.merge(position_grouped, on='Name')

merged_data.to_csv('C:/Users/olive/Documents/All Black Project/Stat_Totals.csv')
