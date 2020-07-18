import numpy as np
import PeakFinder as pf
import matplotlib.pyplot as plt
from matplotlib import style
from numpy.polynomial.polynomial import polyfit

plt.style.use([ 'science', 'ieee', 'no-latex'])
plt.grid(color='black', linestyle='--', linewidth=0.2)

def plot (x,t,p,ma):
    plt.figure(2)
    plt.clf

    plt.xlabel("Tₚ [s]")
    plt.ylabel("ln(xₚ) [arb]")

    plt.title("Logarithm of Position vs. Time Graph")

    if ma == 0:
        runnum = "Run 1 (0g)"
    elif ma == 0.02:
        runnum = "Run 2 (20g)"
    elif ma == 0.04:
        runnum = "Run 3 (40g)"
    elif ma == 0.06:
        runnum = "Run 4 (60g)"
    elif ma == 0.08:
        runnum = "Run 5 (80g)"
    elif ma == 0.1:
        runnum = "Run 6 (100g)"
    elif ma == 0.12:
        runnum = "Run 7 (120g)"

    
    m, b = np.polyfit(t[p], np.log(x[p]), 1)
    print ("Slope = %f, int = %f" %(m, b))

    plt.plot(t[p], np.log(x[p]),'.',  color="navy", markersize=4)

    

    plt.plot(t[p], m*t[p]+b, label=runnum, linestyle='--', color= "black")

    plt.legend(bbox_to_anchor=(1,0.5))
    
    print("b = %f, A0 = %f" %(-m*2*(ma+1.028423), np.exp(b)))

    