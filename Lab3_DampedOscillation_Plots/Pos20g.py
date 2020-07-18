import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import PeakFinder as pf
import PeakAvg as pa
import findingb as fb

mass2 = 0.02

plt.style.use([ 'science', 'ieee', 'no-latex'])

data = pd.read_csv("Lab3Data.csv")

plt.title("Position vs Time")

plt.xlabel("Time [s]")
plt.ylabel("Position [m]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

plt.plot(data.Time, data.Run2, label="Run 2 (20g)", color="navy")

legend = plt.legend(bbox_to_anchor=(1,0.5))

print("Run 2 (20g):")

pf.finder(data.Run2)

pa.avg(data.Time, pf.peaks)

# 'ks' replaces dotted line with points
plt.plot(data.Time[pf.peaks], data.Run2[pf.peaks], 'ks', markersize=1, color='orange')

# finds slope of lnX vs. -b/2m graph and prints initial amplitude and damping coefficient
fb.plot(data.Run2, data.Time, pf.peaks, mass2)

plt.show()