import numpy as np
import pandas as pd

def find_nearest_idx(array, value):
    "find nearest idx in array for the value"
    idx = (np.abs(array - value)).argmin()
    return idx

class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def idx(self, value):
        idx = (np.abs(self - value)).argmin()
        return idx

t_25775 = myarray(np.arange(1.74,2.89,0.01))
fm_25775 = np.zeros_like(t_25775)
fm_25775[0:t_25775.idx(1.92)] = 1.2 #kHz
fm_25775[t_25775.idx(1.92):t_25775.idx(2.1)] = 1.6 
fm_25775[t_25775.idx(2.1):t_25775.idx(2.16)] = 0.8 
fm_25775[t_25775.idx(2.16):t_25775.idx(2.51)] = 1.8 
fm_25775[t_25775.idx(2.51):t_25775.idx(2.56)] = 3.1 
fm_25775[t_25775.idx(2.56):t_25775.idx(2.67)] = 5.4 
fm_25775[t_25775.idx(2.67):] = 6.5 

t_25781 = myarray(np.arange(2.00,5.0,0.01))
fm_25781 = np.zeros_like(t_25781)
fm_25781[0:t_25781.idx(2.25)] = 0.5 #kHz
fm_25781[t_25781.idx(2.25):t_25781.idx(2.57)] = 0.7 
fm_25781[t_25781.idx(2.57):t_25781.idx(2.68)] = 1.0 
fm_25781[t_25781.idx(2.68):t_25781.idx(2.8)] = 0.7 
fm_25781[t_25781.idx(2.8):t_25781.idx(3.06)] = 1.2 
fm_25781[t_25781.idx(3.06):t_25781.idx(3.27)] = 5 
fm_25781[t_25781.idx(3.27):t_25781.idx(4.05)] = 5.6 
fm_25781[t_25781.idx(4.05):] = 11.0


t_25782 = myarray(np.arange(2.21,5.0,0.01))
fm_25782 = np.zeros_like(t_25782)
fm_25782[0:t_25782.idx(2.34)] = 2.4 #kHz
fm_25782[t_25782.idx(2.34):t_25782.idx(2.77)] = 11.0 
fm_25782[t_25782.idx(2.77):t_25782.idx(4.10)] = 10.2 
fm_25782[t_25782.idx(4.10):t_25782.idx(4.68)] = 11.0 
fm_25782[t_25782.idx(4.68):] = 11.6 


t_25783 = myarray(np.arange(1.8,2.5,0.01))
fm_25783 = np.zeros_like(t_25783)
fm_25783[0:t_25783.idx(2.05)] = 1.0 #kHz
fm_25783[t_25783.idx(2.05):t_25783.idx(2.13)] = 2.2
fm_25783[t_25783.idx(2.05):t_25783.idx(2.13)] = 2.2
fm_25783[t_25783.idx(2.13):t_25783.idx(2.18)] = 2.3
fm_25783[t_25783.idx(2.18):t_25783.idx(2.3)] = 1.9
fm_25783[t_25783.idx(2.3):t_25783.idx(2.35)] = 5.5
fm_25783[t_25783.idx(2.35):t_25783.idx(2.39)] = 9.0
fm_25783[t_25783.idx(2.39):] = 10.0


t_25785 = myarray(np.arange(1.7,6.0,0.01))
fm_25785 = np.zeros_like(t_25785)
fm_25785[0:t_25785.idx(2.10)] = 1.0 #kHz
fm_25785[t_25785.idx(2.10):t_25785.idx(2.2)] = 8.2
fm_25785[t_25785.idx(2.2):t_25785.idx(2.71)] = 11.0
fm_25785[t_25785.idx(2.71):t_25785.idx(5.00)] = 12.0
fm_25785[t_25785.idx(5.0):] = 13.0


t_26333 = myarray(np.arange(1.2,2.0,0.01))
fm_26333 = np.zeros_like(t_26333)
fm_26333[0:t_26333.idx(1.50)] = 4.2
fm_26333[t_26333.idx(1.50):t_26333.idx(1.57)] = 6.0
fm_26333[t_26333.idx(1.57):] = 9.5


t_26063 = myarray(np.arange(1.18,4.8,0.01))
fm_26063 = np.zeros_like(t_26063)
fm_26063[0:t_26063.idx(1.50)] = 4.0
fm_26063[t_26063.idx(1.50):t_26063.idx(1.56)] = 6.0
fm_26063[t_26063.idx(1.56):t_26063.idx(2.16)] = 10.0
fm_26063[t_26063.idx(2.16):t_26063.idx(2.41)] = 8.0
fm_26063[t_26063.idx(2.41):t_26063.idx(3.04)] = 10.0
fm_26063[t_26063.idx(3.04):t_26063.idx(3.60)] = 8.0
fm_26063[t_26063.idx(3.60):t_26063.idx(4.31)] = 8.0
fm_26063[t_26063.idx(4.30):] = 6.5


t_26319 = myarray(np.arange(1.49,2.0,0.01))
fm_26319 = np.zeros_like(t_26319)
fm_26319[0:t_26319.idx(1.58)] = 2.2
fm_26319[t_26319.idx(1.58):t_26319.idx(1.66)] = 8.2
fm_26319[t_26319.idx(1.66):] = 10.5


t_26318 = myarray(np.arange(1.54,2.0,0.01))
fm_26318 = np.zeros_like(t_26318)
fm_26318[0:t_26318.idx(1.58)] = 7.5
fm_26318[t_26318.idx(1.58):] = 11


t_26612 = myarray(np.arange(1.62,2.0,0.01))
fm_26612 = np.zeros_like(t_26612)
fm_26612[0:t_26612.idx(1.86)] = 3.5
fm_26612[t_26612.idx(1.86):] = 2.5


t_26717 = myarray(np.arange(1.49,2.0,0.01))
fm_26717 = np.zeros_like(t_26717)
fm_26717[0:t_26717.idx(1.78)] = 9.0
fm_26717[t_26717.idx(1.78):] = 12.0


t_37203 = myarray(np.arange(2.19,4.35,0.01))
fm_37203 = np.zeros_like(t_37203)
fm_37203[0:t_37203.idx(3.24)] = 7.4
fm_37203[t_37203.idx(3.24):t_37203.idx(4.02)] = 7.0
fm_37203[t_37203.idx(4.02):] = 6.5


### ST crash statistics
path = '/afs/ipp/home/o/osam/Sawtooth_crash/new_statistics/'
####
stat_25775 = pd.read_csv(path+'ST_25775_analyzed.txt', sep=" ", header=None)
df_25775 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_25775[0])
for i in range(len(stat_25775[0])):
    idx = find_nearest_idx(t_25775, stat_25775[0][i]) 
    freq_match[i] = fm_25775[idx]

df_25775['time_crash'] = stat_25775[0]
df_25775['ST_crash'] = stat_25775[1]
df_25775['mode_freq'] = freq_match
df_25775['Shot'] = 25775
####
stat_25781 = pd.read_csv(path+'ST_25781_analyzed.txt', sep=" ", header=None)
df_25781 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_25781[0])
for i in range(len(stat_25781[0])):
    idx = find_nearest_idx(t_25781, stat_25781[0][i]) 
    freq_match[i] = fm_25781[idx]

df_25781['time_crash'] = stat_25781[0]
df_25781['ST_crash'] = stat_25781[1]
df_25781['mode_freq'] = freq_match
df_25781['Shot'] = 25781
####
stat_25782 = pd.read_csv(path+'ST_25782_analyzed.txt', sep=" ", header=None)
df_25782 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_25782[0])
for i in range(len(stat_25782[0])):
    idx = find_nearest_idx(t_25782, stat_25782[0][i]) 
    freq_match[i] = fm_25782[idx]

df_25782['time_crash'] = stat_25782[0]
df_25782['ST_crash'] = stat_25782[1]
df_25782['mode_freq'] = freq_match
df_25782['Shot'] = 25782
####
stat_25783 = pd.read_csv(path+'ST_25783_analyzed.txt', sep=" ", header=None)
df_25783 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_25783[0])
for i in range(len(stat_25783[0])):
    idx = find_nearest_idx(t_25783, stat_25783[0][i]) 
    freq_match[i] = fm_25783[idx]

df_25783['time_crash'] = stat_25783[0]
df_25783['ST_crash'] = stat_25783[1]
df_25783['mode_freq'] = freq_match
df_25783['Shot'] = 25783
####
stat_25785 = pd.read_csv(path+'ST_25785_analyzed.txt', sep=" ", header=None)
df_25785 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_25785[0])
for i in range(len(stat_25785[0])):
    idx = find_nearest_idx(t_25785, stat_25785[0][i]) 
    freq_match[i] = fm_25785[idx]

df_25785['time_crash'] = stat_25785[0]
df_25785['ST_crash'] = stat_25785[1]
df_25785['mode_freq'] = freq_match
df_25785['Shot'] = 25785
####
stat_26063 = pd.read_csv(path+'ST_26063_analyzed.txt', sep=" ", header=None)
df_26063 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26063[0])
for i in range(len(stat_26063[0])):
    idx = find_nearest_idx(t_26063, stat_26063[0][i]) 
    freq_match[i] = fm_26063[idx]

df_26063['time_crash'] = stat_26063[0]
df_26063['ST_crash'] = stat_26063[1]
df_26063['mode_freq'] = freq_match
df_26063['Shot'] = 26063
####
stat_26318 = pd.read_csv(path+'ST_26318_analyzed.txt', sep=" ", header=None)
df_26318 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26318[0])
for i in range(len(stat_26318[0])):
    idx = find_nearest_idx(t_26318, stat_26318[0][i]) 
    freq_match[i] = fm_26318[idx]

df_26318['time_crash'] = stat_26318[0]
df_26318['ST_crash'] = stat_26318[1]
df_26318['mode_freq'] = freq_match
df_26318['Shot'] = 26318
####
stat_26319 = pd.read_csv(path+'ST_26319_analyzed.txt', sep=" ", header=None)
df_26319 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26319[0])
for i in range(len(stat_26319[0])):
    idx = find_nearest_idx(t_26319, stat_26319[0][i]) 
    freq_match[i] = fm_26319[idx]

df_26319['time_crash'] = stat_26319[0]
df_26319['ST_crash'] = stat_26319[1]
df_26319['mode_freq'] = freq_match
df_26319['Shot'] = 26319
####
stat_26333 = pd.read_csv(path+'ST_26333_analyzed.txt', sep=" ", header=None)
df_26333 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26333[0])
for i in range(len(stat_26333[0])):
    idx = find_nearest_idx(t_26333, stat_26333[0][i]) 
    freq_match[i] = fm_26333[idx]

df_26333['time_crash'] = stat_26333[0]
df_26333['ST_crash'] = stat_26333[1]
df_26333['mode_freq'] = freq_match
df_26333['Shot'] = 26333
####
stat_26612 = pd.read_csv(path+'ST_26612_analyzed.txt', sep=" ", header=None)
df_26612 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26612[0])
for i in range(len(stat_26612[0])):
    idx = find_nearest_idx(t_26612, stat_26612[0][i]) 
    freq_match[i] = fm_26612[idx]

df_26612['time_crash'] = stat_26612[0]
df_26612['ST_crash'] = stat_26612[1]
df_26612['mode_freq'] = freq_match
df_26612['Shot'] = 26612
####
stat_26717 = pd.read_csv(path+'ST_26717_analyzed.txt', sep=" ", header=None)
df_26717 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_26717[0])
for i in range(len(stat_26717[0])):
    idx = find_nearest_idx(t_26717, stat_26717[0][i]) 
    freq_match[i] = fm_26717[idx]

df_26717['time_crash'] = stat_26717[0]
df_26717['ST_crash'] = stat_26717[1]
df_26717['mode_freq'] = freq_match
df_26717['Shot'] = 26717
####
stat_37203 = pd.read_csv(path+'ST_37203_analyzed.txt', sep=" ", header=None)
df_37203 = pd.DataFrame(columns = ['Shot', 'time_crash', 'ST_crash', 'mode_freq'])
freq_match = np.zeros_like(stat_37203[0])
for i in range(len(stat_37203[0])):
    idx = find_nearest_idx(t_37203, stat_37203[0][i]) 
    freq_match[i] = fm_37203[idx]

df_37203['time_crash'] = stat_37203[0]
df_37203['ST_crash'] = stat_37203[1]
df_37203['mode_freq'] = freq_match
df_37203['Shot'] = 37203
####
frames = [df_25775,df_25781,df_25782,df_25783,df_25785,df_26063,df_26318,df_26319,df_26333,df_26612,df_26717,df_37203]
df = pd.concat(frames, ignore_index=True)
d_repl = {'+':1, '-':0}
df["ST_crash"] = df["ST_crash"].map(d_repl)

#### Save the data frame
df.to_pickle("ST_dataframe.pkl")
