import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import PeakFinder as pf
import PeakAvg as pa
import findingb as fb

mass6 = 0.1

plt.style.use([ 'science', 'ieee', 'no-latex'])

data = pd.read_csv("Lab3Data.csv")

plt.title("Position vs Time")

plt.xlabel("Time [s]")
plt.ylabel("Position [m]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

plt.plot(data.Time, data.Run6, label="Run 6 (100g)", color="navy")

legend = plt.legend(bbox_to_anchor=(1,0.5))

print("Run 6 (100g):")

#finds and stores cell index of each peak
pf.finder(data.Run6)

#finds average of peaks
pa.avg(data.Time, pf.peaks)

# 'ks' replaces dotted line with points
plt.plot(data.Time[pf.peaks], data.Run6[pf.peaks], 'ks', markersize=1, color='orange')

# finds slope of lnX vs. -b/2m graph and prints initial amplitude and damping coefficient
fb.plot(data.Run6, data.Time, pf.peaks, mass6)

plt.show()
