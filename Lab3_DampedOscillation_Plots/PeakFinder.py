peaks = []

def finder(x):
    n = 10
    for i in range(n,len(x)-n):
        if max(x[i-n:i+n]) == x[i]:
            peaks.append(i)
