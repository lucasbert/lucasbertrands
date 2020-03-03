def my_selection_sort(t):
    res=[0]len(t)
    for i in range (len(t)):
        j=index_of_the_smallest_in(t,0,len(t)-1)
        res[i]=t[j]
        t=remove(t,j)
    return res


def remove(t,i):
    res=[0](len(t)-1)
    for j in range (len(t)):
        if j<i:
            res [j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return res

def index_of_the_smallest_in(t,i,j):
   res = i
   for k in range(i+1,j+1):
       if t[res] >t[k]:
           res = k
   return res

t=[5,4,8,1,6,7,9,12,2,1]
res=my_selection_sort(t)