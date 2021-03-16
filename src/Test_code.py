import pandas_datareader as pdr
from datetime import datetime, timedelta, date

# Getting data for Tesla for 20 days
tsla_raw = pdr.get_data_yahoo(symbols='TSLA', start=datetime.now() - timedelta(30), end=datetime.now())

tsla_close = tsla_raw['Close']

# Creating an array
list = []
for i in tsla_close.index:
    list.append(str(tsla_close[i]))

print('\n'.join(list))