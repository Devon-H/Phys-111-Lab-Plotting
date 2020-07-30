import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

print("Run: Lens 3 Only")

flist = []

for i in range(0, len(data.Light3)):

    if(np.isnan(data.Light3[i]) == True):
        continue
    else:
        p = np.float64(data.Lens3only[i] - data.Light3[i])
        q = np.float64(data.Image3[i] - data.Lens3only[i])

        f = (p ** (-1) + q ** (-1)) ** -1

        flist.append(f)
        print(p,q,f)

avg = np.mean(flist)
uncert = np.std(flist)/np.sqrt(len(flist))

print("Avg f3 = %f±%f" %(avg, uncert))