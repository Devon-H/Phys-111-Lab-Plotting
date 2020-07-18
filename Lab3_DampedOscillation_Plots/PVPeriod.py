import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

plt.style.use([ 'science', 'ieee', 'no-latex'])

data = pd.read_csv("Lab3Data.csv")

plt.title("Position and Velocity vs. Time")

plt.xlabel("Time [s]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

plt.plot(data.Time, -1.053495*np.cos(2.13369999*data.Time), label="Position [m]", color="blue", markersize = 3, linestyle = "-")

plt.plot(data.Time, 1.053495*2.13369999*np.sin(2.13369999*data.Time), Label = "Velocity [m/s]", color = "red", markersize = 3, linestyle = "-")

legend = plt.legend(bbox_to_anchor=(1,0.5))

plt.show()
