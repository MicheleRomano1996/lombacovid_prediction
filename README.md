# lombacovid_prediction
Attempt to predict the number of hospitalized in Lombardy according to the historical series of positives / swabs with different apporach:
- XGBoost Regressor with time series method: [lomba_xgb](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_xgb.ipynb)
- XGBoost Regressor with regressive method + exogenous features: [lomba_xgb_regression_reg](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_xgb_regression_reg.ipynb)
- ARIMA: [lomba_ARIMA](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_ARIMA.ipynb)
- SARIMAX: [lomba_SARIMAX](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_SARIMAX.ipynb)
- SARIMAX + exogenous features: [lomba_SARIMAX_temp_hum](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_SARIMAX_temp_hum.ipynb)
- Vector Auto-Regressive Mode VAR: in progress...
- 

# Data
The data (dataframe.csv) of the historical series of hospitalized patients and of the positive / swab ratio were recovered through a script created by [Stefano Martire](https://github.com/virtualmartire); they can be visualized on this [page](https://github.com/virtualmartire/lombacovid). Currently, these data are visible on the website [lombacovid](https://www.lombacovid.it/).

# Exogenous features
In order to improve the metric of different models, I tried to add exogenous variables that could be correlated with the historical time series of the hospitalized. I found interesting as external variables the mean temperature and the mean humidity of Lombardy, both calculated from the average value of the main cities ([here](https://github.com/MicheleRomano1996/lombacovid_prediction/tree/main/Weather)).

# Results
Results are stored in [this file](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/Results.txt).



