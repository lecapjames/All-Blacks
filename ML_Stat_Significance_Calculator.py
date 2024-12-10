import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# This code runs a machine learning model to determine the most impactful team statistics when it comes to winning
# rugby games. The weightings produced by this code are used as weightings for the advanced statistic section.


# import dataset
df = pd.read_csv('C:/Users/olive/Documents/All Black Project/Game_Totals.csv')

# add new column whether the game was won or not.
df['win'] = (df['For'] > df['Against']).astype(int)

# relevant data column
data_cols = [
    "Minutes", "Tries", "Try Assists", "Try Contributions", "Carries", "Meters",
    "Defenders Beaten", "Linebreaks", "Offloads", "Tackles", "Missed Tackles",
    "Turnovers Won", "Turnovers Lost", "Penalties", "Kicks", "Passes",
    "Dominant Tackles"
]

# initialise model variables
X = df[data_cols]
y = df['win']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# initialise model and fit it to data
rf = RandomForestClassifier(max_depth=5, n_estimators=100, bootstrap=False)
rf.fit(X_train, y_train)

# make predictions
y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

# calculate mse and r2 score to analyse model performance
rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

# produce results report
rf_results = pd.DataFrame(['Random forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']

print('Accuracy:', accuracy_score(y_test, y_rf_test_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_rf_test_pred))
print('Classification Report:\n', classification_report(y_test, y_rf_test_pred))

# calculate weightings
z = np.polyfit(y_train, y_rf_train_pred, 1)
p = np.poly1d(z)

feature_importances = rf.feature_importances_
weightings = pd.Series(feature_importances, index=data_cols)

print("Feature Weightings:")
print(weightings)
