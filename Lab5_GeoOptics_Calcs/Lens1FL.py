import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

flist = []

print("Run: Lens 1 Only")

for i in range(0, len(data.Light1)-1):

    if(np.isnan(data.Light1[i]) == True):
        continue
    else:
        p = data.Lens1only[i] - data.Light1[i]
        q = data.Image1[i] - data.Lens1only[i]

        f = (p ** (-1) + q ** (-1)) ** -1

        flist.append(f)
        print(p,q,f)

avg = np.mean(flist)
uncert = np.std(flist)/np.sqrt(len(flist))

print("Avg f1 = %f±%f" %(avg, uncert))
