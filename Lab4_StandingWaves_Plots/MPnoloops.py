import matplotlib.pyplot as plt
from matplotlib import style
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

freq = [Run1, Run2, Run3, Run4, Run5, Run6, Run7, Run8]
runnum = [n1,n2,n3,n4,n5,n6,n7,n8]

plt.clf()

plt.style.use(['science','no-latex'])
fig, axs = plt.subplots(2,4)

fig.suptitle("Frequency vs n", fontsize = 20)

i, j = 0, 0

for k in range(8):

    if(j > 3):
        i = 1
        j = 0
    
    axs[i,j].xaxis.set_major_locator(MultipleLocator(1))
    axs[i,j].xaxis.set_major_formatter(FormatStrFormatter('%d'))

    axs[i,j].yaxis.set_major_locator(MultipleLocator(25))
    axs[i,j].yaxis.set_major_formatter(FormatStrFormatter('%d'))

    axs[i,j].set_title(runname[k])
    axs[i,j].set_xlabel('n')
    axs[i,j].set_ylabel('Frequency [Hz]')

    axs[i,j].grid(which = 'major', color='black', linestyle='-.', linewidth=0.75)
    

    axs[i,j].plot(runnum[k], freq[k], '.', label=runname, color="blue", markersize = 12.5)
    axs[i,j].plot(0,0, '.', color = "red", markersize = 12.5)

    m, b = np.polyfit(runnum[k], freq[k], 1)

    axs[i,j].plot(runnum[k], m*runnum[k]+b, linestyle = '--', color= "green", linewidth= 2.5)

    mu = mass[k]*9.81/(m*2*length[k])**2
    print("%s mu = %f" %(runname[k], mu))


    j+=1



plt.show()