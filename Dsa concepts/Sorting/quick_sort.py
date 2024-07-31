def pivot_place(first,last,data):
    left=first
    right=last-1
    pivot=data[last]
    while True:
        while left<=right and data[left]<=pivot:
            left=left+1
        while left<=right and data[right]>=pivot:
            right=right-1
        if left>right:
            break
        else:
            data[right],data[left]=data[left],data[right]
    
    data[left],data[last]=data[last],data[left] 
    print("Pivot positioned:", data)
    return left
    
def quick_sort(first,last,data):
    if first<last:
        p=pivot_place(first,last,data)
        pivot_place(first,p-1,data)
        pivot_place(p+1,last,data)
        

data=[56,26,93,17,31,44]
quick_sort(0,len(data)-1,data)
print(data)
    
