import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_pickle("ST_dataframe.pkl")
# from collections import Counter
# Counter(df['mode_freq'])

len(df[df['mode_freq'] <= 1.0])
len(df[(df['mode_freq'] > 1.0) & (df['mode_freq'] <= 2.0)])
len(df[(df['mode_freq'] > 2.0) & (df['mode_freq'] <= 4.0)])
len(df[(df['mode_freq'] > 4.0) & (df['mode_freq'] <= 6.0)])
len(df[(df['mode_freq'] > 6.0) & (df['mode_freq'] <= 8.0)])
len(df[(df['mode_freq'] > 8.0) & (df['mode_freq'] <= 10.5)])
len(df[(df['mode_freq'] > 10.5) & (df['mode_freq'] <= 11.0)])
len(df[(df['mode_freq'] > 11.0)])

freq = np.array([1.,3.,5.,7.,9.2,10.7,12.])
stat = np.zeros_like(freq)
df['ST_crash'].value_counts(normalize=True)[1]
stat[0] = df[df['mode_freq'] <= 1.0]['ST_crash'].value_counts(normalize=True)[1]
stat[1] = df[(df['mode_freq'] > 2.0) & (df['mode_freq'] <= 4.0)]['ST_crash'].value_counts(normalize=True)[1]
stat[2] = df[(df['mode_freq'] > 4.0) & (df['mode_freq'] <= 6.0)]['ST_crash'].value_counts(normalize=True)[1]
stat[3] = df[(df['mode_freq'] > 6.0) & (df['mode_freq'] <= 8.0)]['ST_crash'].value_counts(normalize=True)[1]
stat[4] = df[(df['mode_freq'] > 8.0) & (df['mode_freq'] <= 10.5)]['ST_crash'].value_counts(normalize=True)[1]
stat[5] = df[(df['mode_freq'] > 10.5) & (df['mode_freq'] <= 11)]['ST_crash'].value_counts(normalize=True)[1]
stat[6] = df[df['mode_freq'] > 11.0]['ST_crash'].value_counts(normalize=True)[1]

len(freq)
plt.plot(freq,stat,'bo')
plt.show()

