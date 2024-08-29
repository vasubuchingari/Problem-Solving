
def enque():
    if len(l)==length:
        print("stack limit exceeds cannot append")
        return
    element=int(input("Enter element to add : "))
    l.append(element)
    print(l)
    
def deque():
    if not l:
        print("stack is empty")
        return
    l.pop(0)
    print(l)
    
    
l=[]
length=int(input("Enter the length of the stack: "))


while True:
    option=int(input("1)enque 2)deque 3)exit \n"))
    if option==1:
        enque()
    elif option==2:
        deque()
    elif option==3:
        break
    else:
        print("Enter valid Input")
enque()
