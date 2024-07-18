n=int(input("Enter first n fibbonacci :"))
first=0
second=1

for i in range(n):
    if i<2:
        print(i)
    else:
        temp=first+second
        print(temp)
        first=second
        second=temp
