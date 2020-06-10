import datetime

import pandas as pd

START_DATE = datetime.date(2001, 1, 1)
END_DATE = datetime.date(2020, 6, 10)
EMA_PERIOD = 50

dataframe = pd.read_csv('sp500_2000.csv')

for row in dataframe.iloc[252:].itertuples():
    if row.Close < row.Open:
        print(f'{row.Date} is a red day')
        volume_ema = dataframe.iloc[row.Index:row.Index - 50, [6]].Volume.ewm(span=EMA_PERIOD).mean()
        print(volume_ema)
        if row.Volume > volume_ema:
            print(f'Features a volume spike with {row.Volume} > {volume_ema}')
