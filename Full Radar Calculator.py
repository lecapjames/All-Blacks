import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math
data = pd.read_csv("C:/Users/olive/Documents/All Black Project/Per_80_Minute_Avg.csv")


data['Name'] = data['Name'].astype('category')
data['Position'] = data['Position'].astype('category')

#tackles_data = data.groupby("Name").mean().round(2)

#data.groupby("Name").describe().T.round(2).to_csv('C:/Users/olive/Documents/All Black Project/Data_Described.csv')

#sns.set_style("whitegrid")
#pairplot = sns.pairplot(data[["Tries", "Try Assists", "Try Contributions", "Name"]], hue="Name", height=3, palette="Set1")
#pairplot = sns.heatmap(data.corr(), annot=True)
#plt.show()

data = pd.get_dummies(data)

y = data["Meters"]
X = data.drop("Meters", axis=1)

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    train_size = 0.80,
    random_state = 1)

lr = LinearRegression()
lr.fit(X_train,y_train)

print(lr.score(X_test, y_test))
print(lr.score(X_train, y_train))

y_pred = lr.predict(X_test)
print(math.sqrt(mean_squared_error(y_test, y_pred)))

data_new = X_train[:1]
print(lr.predict(data_new))
print(y_train[:1])