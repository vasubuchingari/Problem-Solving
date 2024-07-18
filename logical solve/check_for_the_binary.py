# check for binary
n=int(input("enter a number:"))
while n>0:
    if(n%10!=0 and n%10!=1):
        print("no")
        break
    n=n//10
if(n==0):
    print("yes")
