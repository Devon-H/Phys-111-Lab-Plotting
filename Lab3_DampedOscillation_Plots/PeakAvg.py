period =[]

def avg(t, p):
    ptot = 0.0
    
    for i in range (0,len(p)-1):
        diff = t[p[i+1]]-t[p[i]]

        period.append(diff)

        #print("Period = %f" %diff)

    ptot = sum(period)
    #print("ptot = %f" %(ptot))
    Pavg = ptot/(i+1)

    print("Average Period = %f" %(Pavg))





