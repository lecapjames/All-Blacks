import pandas as pd


# Read in required dataframes
per_80_df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Per_80_Minute_Avg.csv')
stat_totals_df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Stat_Totals.csv')
wins_df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Wins_Data.csv')
non_wins_df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Non_Wins_Data.csv')

per_80_df = per_80_df.drop(per_80_df.columns[0], axis=1)

# Identify columns containing numeric values
data_cols = [
    "Minutes", "Tries", "Try Assists", "Try Contributions", "Carries", "Meters",
    "Defenders Beaten", "Linebreaks", "Offloads", "Tackles", "Missed Tackles",
    "Turnovers Won", "Turnovers Lost", "Penalties", "Kicks", "Passes",
    "Dominant Tackles"
]

# minimum minutes restriction to be considered for an advanced stat
minimum_minutes = 500

# Selects players that meet the minutes requirements
stat_totals_df = stat_totals_df[stat_totals_df['Minutes'] > minimum_minutes]
filtered_player_list = stat_totals_df['Name'].tolist()
filtered_df = per_80_df[per_80_df['Name'].isin(filtered_player_list)]

# Assign weightings
meters_w = 0.110723
linebreaks_w = 0.027604
db_w = 0.017675
offloads_w = 0.037031
tackle_rating_w = 0.032039
t_won_w = 0.087411
penalties_w = 0.031472
tries_w = 0.191399
try_assists_w = 0.082167
try_contributions_w = 0.103932
carry_rating_w = 0.031537
carries_w = 0.031537
t_lost = 0.024282

# Calculate Tackle % and Tackle Rating for each player
filtered_df["Tackle %"] = filtered_df['Tackles']/(filtered_df['Tackles'] + filtered_df['Missed Tackles'])
filtered_df["Tackle Rating"] = filtered_df['Tackles'] * filtered_df['Tackle %']

# Calculate Carry Rating
filtered_df["Carry Rating"] = (meters_w * filtered_df["Meters"] + linebreaks_w * filtered_df["Linebreaks"] + db_w * filtered_df["Defenders Beaten"] + offloads_w * filtered_df["Offloads"])/filtered_df["Carries"]
data_cols.append(["Tackle %", "Tackle Rating", "Carry Rating"])

# Normalise all the numerical data so it falls between 0 and 1
norm_df = filtered_df.copy()
for column in data_cols:
    max_value = norm_df[column].max()
    min_value = norm_df[column].min()
    norm_df[column] = (filtered_df[column] - min_value) / (max_value - min_value)

# Calculate Offensive and Defensive Rating
filtered_df["Defensive Rating"] = 100*(tackle_rating_w * norm_df["Tackle Rating"] + t_won_w * norm_df["Turnovers Won"] - penalties_w * norm_df["Penalties"])
filtered_df["Offensive Rating"] = 100*(tries_w * norm_df["Tries"] + try_assists_w * norm_df["Try Assists"] + try_contributions_w * norm_df["Try Contributions"] + carry_rating_w * norm_df["Carry Rating"] + carries_w * norm_df["Carries"] - t_lost * norm_df["Turnovers Lost"])

# Normalise Offensive and Defensive Rating
for column in ["Defensive Rating", "Offensive Rating"]:
    max_value = filtered_df[column].max()
    min_value = filtered_df[column].min()
    norm_df[column] = (filtered_df[column] - min_value) / (max_value - min_value)

# Assign weightings
offensive_w = 0.5
defensive_w = 0.5

# Calculate Player Rating
filtered_df["Player Rating"] = 100 * (offensive_w * norm_df["Offensive Rating"] + defensive_w * norm_df["Defensive Rating"])

advanced_df = filtered_df[["Name", "Tackle %", "Tackle Rating", "Carry Rating", "Defensive Rating", "Offensive Rating", "Player Rating"]].copy()
advanced_df.to_csv('C:/Users/olive/Documents/All Black Project/Advanced_Statistics.csv')
