import datetime

import pandas as pd

START_DATE = datetime.date(2001, 1, 1)
END_DATE = datetime.date(2020, 6, 10)
EMA_PERIOD = 50

dataframe = pd.read_csv('sp500_2000.csv')
volume_ema = dataframe.loc[:, ['Volume']].ewm(span=200).mean()
price_ema = dataframe.loc[:, ['Close']].ewm(span=EMA_PERIOD).mean()

for row in dataframe.iloc[252:].itertuples():
    if row.Close < row.Open:
        if price_ema.Close[row.Index] > row.Close:
            # Volume is 7th column
            volume_avg = dataframe.iloc[row.Index - EMA_PERIOD:row.Index, [6]].mean()
            if volume_avg.Volume * 1.5 < row.Volume:
                print(f'{row.Date} is a red day')
                print(f'Price below EMA {row.Close} < {price_ema.Close[row.Index]}')
                print(f'Volume spike detected, buy here')
