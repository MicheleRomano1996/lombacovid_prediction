# lombacovid_prediction
Attempt to predict the number of hospitalized in Lombardy according to the historical series of positives / swabs with different apporach:
- XGBoost Regressor with time series method: [lomba_xgb](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_xgb.ipynb)
- XGBoost Regressor with regressive method: [lomba_xgb_regression_reg](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_xgb_regression_reg.ipynb)
- SARIMA: [lomba_ARIMA](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_ARIMA.ipynb)
- SARIMAX: [lomba_SARIMAX](https://github.com/MicheleRomano1996/lombacovid_prediction/blob/main/lomba_SARIMAX.ipynb)
- Vector Auto-Regressive Mode VAR: 
- 

# Data
The data (story.csv) of the historical series of hospitalized patients and of the positive / swab ratio were recovered through a script created by [Stefano Martire](https://github.com/virtualmartire); they can be visualized on this [page](https://github.com/virtualmartire/lombacovid). Currently, these data are visible on the website [lombacovid](https://www.lombacovid.it/).
 

