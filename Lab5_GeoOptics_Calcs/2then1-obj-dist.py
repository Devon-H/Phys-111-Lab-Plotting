import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

print("Run: Lens 2 then 1")
pError = []
Llist = []
f1 = 309.458691
f2 = 311.125255

for i in range(0, len(data.Light2then1)-1):

    if(np.isnan(data.Light2then1[i]) == True):
        continue
    else:
        p2 = data.Lens2before1[i] - data.Light2then1[i]
        L = data.Lens1after2[i] - data.Lens2before1[i]
        q1meas = data.Image2then1[i] - data.Lens1after2[i]

        q1theo = (f1**(-1)-(L-(f2 ** (-1) - p2 ** (-1))**-1)**-1)**-1


        pE = np.abs(100 - q1theo/q1meas*100)

        pError.append(pE)

        print("L = %f, q1 theory = %f, q1 measured = %f" %(L, q1theo, q1meas))

avg = np.mean(pError)
print("Average Percent Error = %f" %(avg))