def remove(t,i):
    res=[0]*(len(t)-1)
    for j in range(len(t)):
        if j<i:
            res[j]=t[j]
        if j>i:
            res[j-1]=t[j]
    return res
