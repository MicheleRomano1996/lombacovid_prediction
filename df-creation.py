# creazione del dataframe con i dati di lombacovid e temperatura/umidità media dai file .csv nella cartella Weather


import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def datatransform(data):
    data['Data'] = pd.to_datetime(data['Data'],dayfirst=True)
    data = data.sort_values('Data',ascending=True)
    data = data.groupby(pd.Grouper(key='Data', freq='1D')).mean()
    data = data.iloc[6: , :]  # seleziono i valori dal 08-09-2022
    for k in data.columns: 
        data[k].fillna(method='bfill',inplace=True)  # fill NaN with method bfill
    return data

# creazione dataframe

# read file via lombacovid.it
data = pd.read_csv('https://www.lombacovid.it/story.csv',usecols = ['data','perc_story','ospedalizzati_story'])

data['data'] = pd.to_datetime(data['data'], dayfirst=True)
data.rename(columns = {'ospedalizzati_story':'ospedalizzati_oggi',
                       'perc_story':'perc_oggi',
                       'data':'date'},
                            inplace = True)
data.set_index('date',inplace=True)

# perc_oggi smoothed by running average of 7 days
running_average = 7     
data['perc_oggi'] = data['perc_oggi'].rolling(window=running_average).mean()
data = data.dropna()


# adding mean temperature and humidity of lombardy from 01/09/2020 to 03/09/2020

Bergamo_airport_ts = pd.read_csv('Weather/Bergamo_airport_ts.csv')
Bergamo_airport_ts = datatransform(Bergamo_airport_ts)

Brescia_airport_ts = pd.read_csv('Weather/Brescia_airport_ts.csv')
Brescia_airport_ts = datatransform(Brescia_airport_ts)

Milan_airport_ts = pd.read_csv('Weather/Milan_airport_ts.csv')
Milan_airport_ts = datatransform(Milan_airport_ts)

Milan_malpensa_ts = pd.read_csv('Weather/Milan_malpensa_ts.csv')
Milan_malpensa_ts = datatransform(Milan_malpensa_ts)

Milan_ts = pd.read_csv('Weather/Milan_ts.csv')
Milan_ts = datatransform(Milan_ts)

Piacenza_ts = pd.read_csv('Weather/Piacenza_ts.csv')
Piacenza_ts = datatransform(Piacenza_ts)

Verona_ts = pd.read_csv('Weather/Verona_ts.csv')
Verona_ts = datatransform(Verona_ts)

dataframe = [Bergamo_airport_ts,
Brescia_airport_ts,
Milan_airport_ts,
Milan_malpensa_ts,
Milan_ts,
Piacenza_ts,
Verona_ts]

temp_ts = pd.DataFrame()
umid_ts = pd.DataFrame()
final_ts = pd.DataFrame()

num = 0
for i in dataframe:
    temp_ts['Temperatura '+str(num)] = i.Temperatura
    num += 1 
    
num = 0
for i in dataframe:
    umid_ts['Umidutà '+str(num)] = i.Umidità
    num += 1 

final_ts['Temperatura_media'] =  temp_ts.sum(axis=1)/len(temp_ts.columns)
final_ts['Umidità_media'] = umid_ts.sum(axis=1)/len(temp_ts.columns)

for i in final_ts:
    data[i] = final_ts[i]
    
data = data[data.index <= '2022-09-03']

data.to_csv('dataframe.csv')
