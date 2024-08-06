l=[3,1,-7,7,9,0,5,8888,5,5]
for i in range(len(l)-1):
    min_index=i
    for j in range(i+1,len(l)):
        if(l[min_index]>l[j] ):
            min_index=j
        
    l[i],l[min_index]=l[min_index],l[i]
print(l)
            
        
        
    
