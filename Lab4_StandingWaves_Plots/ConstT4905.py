import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

runname = ["Run 1", "Run 2","Run 3", "Run 4", "Run 5", "Run 6", "Run 7", "Run 8"]
length = [1.67, 1.67, 1.32, 1.32, 1.09, 1.09, 1.09, 0.94]
mass = [0.2, 0.4, 0.4, 0.5, 0.5, 0.3, 0.1, 0.1]

n1 = np.float64([0,2,3,4,5,6])
Run1 = [0,28.1,42,55.8,70.3,83.5]

n2 = np.float64([0,1,2,3,4])
Run2 =[0,20.3,40.1,59.6,78.5]

n3 = np.float64([0,1,2,3,4])
Run3 = [0,24.6, 51, 75.2, 100.3]

n4 = np.float64([0,1,2,3])
Run4 = [0,29.8,57.8,84.9]

n5 = np.float64([0,1,2])
Run5 = [0,35.7,68.5]

n6 = np.float64([0,1,2,3,4])
Run6 = [0,26.7,54,78.4,105.9]

n7 = np.float64([0,1,2,3,4,5])
Run7 = [0,16.7,33.6,49.1,62.7,78]

n8 = np.float64([0,1,2,3,4]) 
Run8 = [0,17.5,38,53.6,73]

plt.style.use([ 'science', 'ieee','no-latex'])

fig, axs = plt.subplots(1,1)

axs.xaxis.set_major_locator(MultipleLocator(1))
axs.xaxis.set_major_formatter(FormatStrFormatter('%d'))

axs.yaxis.set_major_locator(MultipleLocator(25))
axs.yaxis.set_major_formatter(FormatStrFormatter('%d'))

axs.set_title("Frequency vs. n (T = 4.905N)")
axs.set_xlabel('n')
axs.set_ylabel('Frequency [Hz]')

axs.grid(which = 'major', color='black', linestyle='-.', linewidth=0.25)

axs.plot(n4, Run4,'.', label="Run 4 (132cm)", color="purple")
axs.plot(n5,Run5,'.', label = "Run 5 (109cm)", color = "green")

legend = plt.legend(fontsize = 'small', loc = "upper left", frameon= 'true')

plt.show()