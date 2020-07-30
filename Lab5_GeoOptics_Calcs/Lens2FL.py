import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

print("Run: Lens 2 Only")

flist = []

for i in range(0, len(data.Light2)-1):

    if(np.isnan(data.Light2[i]) == True):
        continue
    else:
        p = data.Lens2only[i] - data.Light2[i]
        q = data.Image2[i] - data.Lens2only[i]

        f = (p ** (-1) + q ** (-1)) ** -1

        flist.append(f)
        print(p,q,f)

avg = np.mean(flist)
uncert = np.std(flist)/np.sqrt(len(flist))

print("Avg f2 = %f±%f" %(avg, uncert))