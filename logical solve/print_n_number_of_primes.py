n = int(input("Enter a number: "))

tot = 0
count = 2

while tot!=  n:
    for i in range(2, (count // 2) + 1):
        #if not else
        if count % i == 0:
            #for loop breaks
            break
    else:
        print(count,end=" ")
        tot += 1
    count += 1

    

    
    
