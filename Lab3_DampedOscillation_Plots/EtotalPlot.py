import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

omega = [2.13369999, 2.306763433, 2.27445622, 2.008833526, 2.081613303, 2.163905518, 2.129893324]
inita = [1.053485, 1.099028, 1.096609, 1.093565, 1.123014, 1.117406, 1.107279]
ma = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12]
runnum = ["Run 1 (0g)", "Run 2 (20g)", "Run 3 (40g)", "Run 4 (60g)", 
        "Run 5 (80g)","Run 6 (100g)", "Run 7 (120g)"]
col = ["black", "red", "green", "blue", "maroon", "navy", "purple"]

k = 5.097292 
b = 0.002804857
mi = 1.028423 

data = pd.read_csv("Lab3Data.csv")

plt.style.use([ 'science', 'ieee', 'no-latex'])

plt.figure(1)
plt.clf

plt.title("Total Energy vs. Time")

plt.xlabel("Time [s]")
plt.ylabel("Eₜ [J]")

plt.grid(color='black', linestyle='--', linewidth=0.2)

for i in range (0,len(inita)):
    plt.plot(data.Time, 0.5*k*inita[i]**2*np.exp(-b*data.Time/(mi +ma[i])) , label=runnum[i], color = col[i], linestyle = '-')

legend = plt.legend(bbox_to_anchor=(1,0.5))
plt.show()
