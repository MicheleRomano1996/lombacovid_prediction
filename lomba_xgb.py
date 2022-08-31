import pandas as pd
import numpy as np
from math import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor, plot_importance
from sklearn.model_selection import RepeatedKFold,StratifiedKFold,GridSearchCV

import warnings
warnings.filterwarnings("ignore")


# definzioni funzioni varie
def timeserieFeatureExtractor(timeseries):
    timeseries['dayofweek'] = timeseries.index.dayofweek
    timeseries['quarter'] = timeseries.index.quarter
    timeseries['month'] = timeseries.index.month
    timeseries['year'] = timeseries.index.year
    timeseries['dayofyear'] = timeseries.index.dayofyear
    timeseries['dayofmonth'] = timeseries.index.day
    timeseries['weekofyear'] = timeseries.index.weekofyear
    timeseries['daysinmonth'] = timeseries.index.daysinmonth
    timeseries['weekend'] = np.where(timeseries.index.dayofweek > 4, 1, 0)
    timeseries.fillna(0,inplace=True)
    return 

def calcError(y_test, y_pred):
    R2 = r2_score(y_test, y_pred)
    MSE = mean_squared_error(y_test, y_pred)
    RMSE = sqrt(MSE)
    MAE = mean_absolute_error(y_test, y_pred)
    MAPE = mean_absolute_percentage_error(y_test, y_pred)
    print(f'R2: {R2}')
    print(f'Mean Squared Error: {MSE}')
    print(f'Root Mean Sqarred Error: {RMSE}')
    print(f'Mean Absolute Error: {MAE}')
    print(f'Mean Absolute Percentage Error: {MAPE}')
    return

# -> construction of the dataframe
data = pd.read_csv('https://www.lombacovid.it/story.csv',usecols = ['data','perc_story','ospedalizzati_story'])
data['data'] = pd.to_datetime(data['data'], dayfirst=True)
data.rename(columns = {'ospedalizzati_story':'ospedalizzati_oggi',
                       'perc_story':'perc_oggi',
                       'data':'date'},
                            inplace = True)
data.set_index('date',inplace=True)

# -> feature engineering 
# on perc_oggi smoothed by running average of 7 days
running_average = 7     
data['perc_oggi'] = data['perc_oggi'].rolling(window=running_average).mean()
data = data.dropna()

# creation of ospedalizzati and perc_oggi lag features shifted by 7 days: t, t+1, ... t+n
past_days = 14           # <---
for i in range(1, past_days):
    data[f'ospedalizzati_past{i}'] = data['ospedalizzati_oggi'].shift(i).fillna(0)
for i in range(1, past_days):
    data[f'perc_past{i}'] = data['perc_oggi'].shift(i).fillna(0)

# creation of the target: ospedalizzati_oggi lagged by 7 days in the future: t-7
future_target = 7       # <---
data['ospedalizzati_target'] = data['ospedalizzati_oggi'].shift(-future_target).fillna(0)
data = data.fillna(0)

# -> feature extraction
timeserieFeatureExtractor(data)

# -> model section
# calculate train, test and validation length
len_train_train_test = int(len(data.index)-len(data.index)*20/100)
separation_index_train_test = list(data.index)[len_train_train_test]

len_train_val = int(len_train_train_test-len_train_train_test*20/100)
separation_index_train_val = list(data.index)[len_train_val]

# feature splitting and plot
X = data.drop(columns='ospedalizzati_target')
X_train = X[X.index < separation_index_train_val]
X_val = X[(X.index > separation_index_train_val) & (X.index < separation_index_train_test)]
X_test = X[X.index > separation_index_train_test]

plt.figure(figsize=(13,8))
plt.plot(X_train['ospedalizzati_oggi'],color='green',label='train set')
plt.plot(X_val['ospedalizzati_oggi'],color='blue',label='validation set')
plt.plot(X_test['ospedalizzati_oggi'],color='red',label='test set')
plt.axvline(x=separation_index_train_test, ymin = 0.02, ymax = 0.6, color='orange')
plt.axvline(x=separation_index_train_val, ymin = 0.02, ymax = 0.6, color='orange')
plt.title('ospedalizzati_oggi speration')
plt.legend(prop={'size': 12})
plt.show()

# target splitting and plot
y = data['ospedalizzati_target']
y_train = y[y.index < separation_index_train_val]
y_val = y[(y.index > separation_index_train_val) & (data.index < separation_index_train_test)]
y_test = y[y.index > separation_index_train_test]

# fitting the model
model = XGBRegressor(booster = 'gbtree',
                     eval_metric = 'rmse',
                     objective = 'reg:squarederror',
                     eta = 0.1,
                     min_child_weight = 1,
                     max_depth = 6,
                     max_delta_step = 0,
                     subsample = 1,
                     colsample_bytree = 0.8,
                     colsample_bylevel = 1,
                     scale_pos_weight = 1,
                     gamma = 1,
                     reg_lambda = 0.5,
                     reg_alpha = 1,
                     n_estimators = 500,
                     seed = 42)
model.fit(X_train, y_train)

# prediction
y_pred_val = model.predict(X_val)

# feature importance of xgboost
plot_importance(model,height=0.5,max_num_features = 20)
plt.show()

# error on the first prediction 
print('Error on validation data')
calcError(y_val,y_pred_val)

# plot train vs val
plt.figure(figsize=(13,8))
plt.plot(y_val.values,label='validation')
plt.plot(y_pred_val,label='prediction')
plt.legend(prop={'size': 12})
plt.title('Before tuning hyperparams')
plt.show()


# -> tuning model parameters
