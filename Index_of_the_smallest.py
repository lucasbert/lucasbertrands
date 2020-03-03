def index_of_the_smallest(list,start,stop):
    index=0
    if start >= stop:
        fin=start
        debut=stop
    else:
        fin=stop
        debut=start
    for  element in list:
        if element >= debut and element <= fin:
            print (index)
            index +=1
        else:
            index +=1
            
            
            
            
            
            
            
            
            
            
            
            
            
            def selection_sort(t):
   n= len(t)
   res = [0]*n
   for k in range(0,n-1):
      index=index_of_the_smallest_in(t,0,len(t)-1)
      res[k]=t[index]
      t=remove(t,index)
  return res