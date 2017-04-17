import numpy as np
import pandas as pd

df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s=IBM')

date_filter = (df['Date'] >= '2005-01-01') & (df['Date'] <= '2005-12-31')
sample = df.loc[date_filter]

min_c = np.min(sample['Close'])
max_c = np.max(sample['Close'])
med_c = np.median(sample['Close'])

print "2005-01-01 - 2005-12-31"
print 'Min: {}  Max: {}  Median: {}'.format(min_c, max_c, med_c)

close = sample['Close']

print 'Min: {}  Max: {}  Median: {}'.format(
    close.min(), close.max(), close.median())
print close.describe()

df['Date'] = pd.to_datetime(df['Date'])
df[df.Date.dt.year == 2005]['Close'].describe()
