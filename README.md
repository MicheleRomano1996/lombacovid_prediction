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
 
# Results (02/09/2022)
- XGBoost (time series method):
* 2022-09-02	650.687195
* 2022-09-03	658.080750
* 2022-09-04	622.649597
* 2022-09-05	652.914368
* 2022-09-06	674.797974
* 2022-09-07	649.902100
* 2022-09-08	624.360962

- XGBoost (regressive method):
* updating...

- SARIMA:
* 2022-09-03    588.894011
* 2022-09-04    549.206814
* 2022-09-05    546.442726
* 2022-09-06    548.010702
* 2022-09-07    534.309148
* 2022-09-08    520.779589
* 2022-09-09    508.286188

- SARIMAX:
* 2022-09-03    594.767089
* 2022-09-04    567.833526
* 2022-09-05    539.326673
* 2022-09-06    492.894896
* 2022-09-07    454.212628
* 2022-09-08    412.283800
* 2022-09-09    369.123933
