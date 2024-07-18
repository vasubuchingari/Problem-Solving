#eg 6 because 1,2,3 ==6 (proper divisors)
n=int(input("enter a number: "))
tot=0
for i in range (1,n//2+1):
    if n%i==0:
        tot=tot+i
        print(tot)
if tot==n:
    print("yes")
else:
    print("no")
    
