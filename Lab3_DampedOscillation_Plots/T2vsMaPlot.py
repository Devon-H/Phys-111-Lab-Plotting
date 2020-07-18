import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import PeakFinder as pf
import PeakAvg as pa
import numpy as np
from numpy.polynomial.polynomial import polyfit

ma = np.float64([0, 20, 40, 60, 80, 100, 120])
t2 = [8.671475999, 7.419140916, 6.890625, 9.782995217, 9.110865333, 8.431078791, 8.7025]

plt.style.use([ 'science', 'ieee', 'no-latex'])

data = pd.read_csv("Lab3Data.csv")

plt.title("Time² vs Mass Added")

plt.xlabel("Added Mass [g]")
plt.ylabel("T² [s²]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

# plt.xticks(np.linspace(0, 140, 1))
# plt.yticks(np.linspace(5, 10, 1))


plt.plot(ma, t2, '.', color="blue", markersize=3)

m, b = np.polyfit(ma, t2, 1)
print(m,b)

k = 4*np.pi**2/(m*1000.0)

print("k = %f" %(k))
print("m0 = %f" %(b*k/(4*np.pi**2)))
plt.plot(ma, m*ma+b, linestyle='--')

plt.show()
