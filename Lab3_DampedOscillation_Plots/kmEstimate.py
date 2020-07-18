import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import PeakFinder as pf
import numpy as np

plt.style.use([ 'science', 'ieee', 'no-latex'])

data = pd.read_csv("Lab3Data.csv")

plt.title("Position vs Time")

plt.xlabel("Time [s]")
plt.ylabel("Position [m]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

plt.plot(data.Time, data.FromRest, color="red", Label = "From Rest")

pf.finder(data.FromRest)

plt.plot(data.Time[pf.peaks], data.FromRest[pf.peaks], 'ks', markersize=1, color='navy')

legend = plt.legend(bbox_to_anchor=(1,0.5))

for i in pf.peaks:
    print("x = %f, t = %f" %(data.FromRest[i], data.Time[i]))

plt.show()
