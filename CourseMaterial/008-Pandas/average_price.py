import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s=IBM')

print df.loc[df['Date'].isin(['2009-06-30'])]
print 'June 30, 2009 is in Row 1.'

avg_price = np.average([df.loc[1, 'High'], df['Low'][1]])
print 'Average price: ', avg_price


df.index = pd.to_datetime(df['Date'])
print df.loc[datetime(2009,6,30),['High', 'Low']].mean()
