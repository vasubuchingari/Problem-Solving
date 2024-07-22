stack=[]
def push():
    if len(stack)==n:
        print("the stack is full reached its limits")
    else:
        element=input("enter the push element: ")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("the stack is empty")
    else:
        print("Popped element is :" ,stack[-1])
        stack.pop()
        print(stack)

n=int(input("enter total number of elements in the stack: "))
while True:
    print("lets start the stack operations: \n 1)push \n 2)pop \n 3)quit   ")
    inp=int(input("please enter the input: "))
    if inp==1:
        push()
    elif inp==2:
        pop()
    elif inp==3:
        print("tnx for the operations")
        break
    else:
        print("oops wrong input")
    
    
    
