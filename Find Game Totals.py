import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('C:/Users/olive/Documents/All Black Project/ALLBLACKDATA.csv')

# Define the columns that contain the statistics
data_cols_to_sum = [
    "Minutes", "Tries", "Try Assists", "Try Contributions", "Carries", "Meters",
    "Defenders Beaten", "Linebreaks", "Offloads", "Tackles", "Missed Tackles",
    "Turnovers Won", "Turnovers Lost", "Penalties", "Kicks", "Passes", "Dominant Tackles"
]

# Define the columns to keep as is
data_cols_to_keep = ["For", "Against", "Posession", "Territory"]

# Group by 'Date' and aggregate
df_grouped = df.groupby('Date').agg({col: 'sum' for col in data_cols_to_sum})
df_grouped = df_grouped.reset_index()

# Add the columns to keep as is
df_keep = df.groupby('Date')[data_cols_to_keep].first().reset_index()
df_grouped = pd.merge(df_grouped, df_keep, on='Date')

# Save or view the new DataFrame
df_grouped.to_csv('C:/Users/olive/Documents/All Black Project/Game_Totals.csv', index=False)
print(df_grouped)
