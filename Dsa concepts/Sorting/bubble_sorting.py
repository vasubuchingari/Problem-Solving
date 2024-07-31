l=[5,4,3,2,1]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            print(l)
        else:
            print(l)
    print()
