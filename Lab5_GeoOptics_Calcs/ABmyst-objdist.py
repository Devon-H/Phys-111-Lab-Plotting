import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

data = pd.read_csv("Lab5Data.csv")

pError = []
qBlist = []
runname = ["Run: 1-2, 1-3, 1-D", "Run: 2-1, 2-3, 2-D", "Run: 3-1, 3-2, 3-D", "Run: D-1, D-2, D-3"]
name1 = ["(1-2)", "(1-3)", "(1-D)"]
name2 = ["(2-1)", "(2-3)", "(2-D)"]
name3 = ["(3-1)", "(3-2)", "(3-D)"]
named = ["(D-1)", "(D-2)", "(D-3)"]
namelist = [name1, name2, name3, named]

primeflist = [309.458691, 311.125255, 188.929472, -397.956928 ]

flist1 = [311.125255, 188.929472, -397.956928]
flist2 = [309.458691, 188.929472, -397.956928]
flist3 = [309.458691, 311.125255, -397.956928]
flistd = [309.458691, 311.125255, 188.929472]

secondflist = [flist1, flist2, flist3, flistd]

# 1-2, 1-3, 1-D object distances with average error for each
for j in range(0,4):
    print("%s" %(runname[j]))
    for k in range(0, 3):
        for i in range(0, len(data.LightAthenB)-1):

            if(np.isnan(data.LightAthenB[i]) == True):
                continue
            else:
                pA = data.LensA[i] - data.LightAthenB[i]
                L = data.LensB[i] - data.LensA[i]
                qBmeas = data.ImageAthenB[i] - data.LensB[i]

                qBtheo = (secondflist[j][k]**(-1)-(L-(primeflist[j] ** (-1) - pA ** (-1))**-1)**-1)**-1

                pE = np.abs(qBtheo-qBmeas)/qBmeas*100

                pError.append(pE)

                qBlist.append(np.round(qBtheo,3))

                np.savetxt("Lab5Eval.csv", qBlist, delimiter=",", fmt = "%.3f")

                #print("qB %s  = %.3f, qB measured = %f" %(namelist[j][k], np.round(qBtheo,3), qBmeas))

        avg = np.mean(pError)
        pError.clear()

        print("Average Percent Error %s = %f" %(namelist[j][k], avg))
             
    print("\n")