# Getting data from repo and assigning it to X- Features Y- Targets
from ucimlrepo import fetch_ucirepo

# fetch dataset
mushroom = fetch_ucirepo(id=73)

# data (as pandas dataframes)
X = mushroom.data.features
Y = mushroom.data.targets

# metadata
# print(mushroom.metadata)

# variable information
# print(mushroom.variables)
print(X)


#Training and testing
X_train = train.loc[:, features] # the TRAINING dataset with explanatory features
y_train = train['medv'] # the TRAINING set with the feature we want to learn to predict.

X_test = test.loc[:, 'crim':'lstat'] # the TEST set with the explanatory features
y_test= test['medv'] # the TEST set with the feature we want to learn to predict.


from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train,y_train)

predictions = model.predict(X_test)

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print('RMSE = ', rmse)

import pickle

pickle.dump(model, open('our_model.sav', 'wb'))
print('...Model saved...')