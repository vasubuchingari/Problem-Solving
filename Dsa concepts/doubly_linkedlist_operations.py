class node():
    def __init__(self,value):
        self.value=value
        self.previous=None
        self.next=None

class DLL():
    def __init__(self):
        self.head=None
    
    def printDll(self):
        if self.head is None:
            print("the DLL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.value,"-->",end="")
                n=n.next
                
    def printDllRev(self):
        if self.head is None:
            print("no DLL list fount")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            
            while n is not None:
                print(n.value,"<--",end="")
                n=n.previous
                
    
    def addBegin(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
    
    def addEnd(self,value):
        new_node=node(value)
        if self.head is None:
            print("the dll is empty")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            new_node.previous=n
            
    def addAfter(self,value,x):
        new_node=node(value)
        if self.head is None:
            print("the dll is empty")
        else:
            n=self.head
            while n is not None:
                if n.value==x:
                    break
                n=n.next
            if n is None:
                print("the number to add after is not present")
            else:
                new_node.next=n.next
                new_node.previous=n
                if n.next is not None:
                    n.next.previous=new_node
                n.next=new_node

            
                
            

dll=DLL()
dll.printDll()
print("add BEGIN")
dll.addBegin(30)
dll.addBegin(40)
dll.addBegin(50)
dll.printDll()
print("\nadd END")
dll.addEnd(1)
dll.addEnd(2)
dll.addEnd(3)
dll.printDll()
print("\nadd AFTER")
dll.addAfter(0,1)
dll.addAfter(0,2)
dll.addAfter(0,3)
dll.printDll()
print("\nREVERSED LIST")
dll.printDllRev()






#result

the DLL is empty
add BEGIN
50 -->40 -->30 -->
add END
50 -->40 -->30 -->1 -->2 -->3 -->
add AFTER
50 -->40 -->30 -->1 -->0 -->2 -->0 -->3 -->0 -->
REVERSED LIST
0 <--3 <--0 <--2 <--0 <--1 <--30 <--40 <--50 <--




















