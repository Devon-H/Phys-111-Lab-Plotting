import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

flist = []
fcsvlist = []

print("Run: Diverging Lens then Lens 1")

f1 = 309.458691

for i in range(0, len(data.LightDthen1)-1):

    if(np.isnan(data.LightDthen1[i]) == True):
        continue
    else:
        pd = data.LensDbefore1[i] - data.LightDthen1[i]
        L = data.Lens1afterD[i] - data.LensDbefore1[i]
        q1 = data.ImageD[i] - data.Lens1afterD[i]

        fd = ((L-(f1 ** (-1) - q1 ** (-1)) ** (-1)) ** (-1) + pd ** (-1)) ** -1

        flist.append(fd)
        fcsvlist.append(np.round(fd, 3))

        np.savetxt("Lab5DivFL.csv", fcsvlist, delimiter=",", fmt = "%.3f")

        print(L,fd)

avg = np.mean(flist)
uncert = np.std(flist)/np.sqrt(len(flist))

print("Avg fd = %f±%f" %(avg, uncert))