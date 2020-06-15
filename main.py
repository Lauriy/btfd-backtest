import datetime

import pandas as pd

START_DATE = datetime.date(2001, 1, 1)
END_DATE = datetime.date(2020, 6, 10)
EMA_PERIOD = 200
VOLUME_SPIKE_WINDOW = 20

dataframe = pd.read_csv('SPY.csv')
price_ema = dataframe.loc[:, ['Close']].ewm(span=EMA_PERIOD).mean()

for row in dataframe.iloc[252:].itertuples():
    if price_ema.Close[row.Index] > row.Close:
        # Volume is 7th column
        volume_avg = dataframe.iloc[row.Index - VOLUME_SPIKE_WINDOW:row.Index, [6]].mean()
        # 50% higher volume
        if volume_avg.Volume * 1.5 < row.Volume:
            print(f'{row.Date}')
