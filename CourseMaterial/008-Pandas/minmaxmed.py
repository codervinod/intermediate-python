import numpy as np
import pandas as pd

df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s=IBM')

min_c = np.min(df['Close'])
max_c = np.max(df['Close'])
med_c = np.median(df['Close'])

print 'Min: {}  Max: {}  Median: {}'.format(min_c, max_c, med_c)


close = df['Close']

print 'Min: {}  Max: {}  Median: {}'.format(
    close.min(), close.max(), close.median())
print close.describe()


print 'Min: {min}, Max: {max}, Median: {50%}'.format(
    **close.describe().to_dict())