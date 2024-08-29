class node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    def printLL(self):
        n = self.head
        if n is None:
            print("The linked list is empty!")
        else:
            while n is not None:
                print(n.value, "-> ", end="")
                n = n.next
            print()

    def addBegin(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        
    def addEnd(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    def addAfter(self,value,x):
        new_node=node(value)
        if self.head is None:
            print("the ll is empty")
        else:
            n=self.head
            while n is not None:
                if n.value==x:
                    break
                n=n.next
            if n is None:
                print(f"{x} the node is not present")
            else:
                new_node.next=n.next
                n.next=new_node
                
    def addBefore(self,value,x):
        new_node=node(value)
        if self.head is None:
            print("the LL is empty")
        elif self.head.value==x:
            new_node.next=self.head
            self.head=new_node
        else:
            n=self.head

            while n.next is not None:#we should check n.next cause we are accessing
                if n.next.value==x:
                    break
                n=n.next
            if n.next is None:
                print(f"{x}  value is found")
            else:
                
                new_node.next=n.next
                n.next=new_node
                
    def delStart(self):
        if self.head is None:
            print("the LL is empty")
        else:
            self.head=self.head.next
    def delEnd(self):
        if self.head is None:
            print("the LL is empty")
        elif self.head.next is None:
            self.head=None
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
    
    def delAny(self,x):
        if self.head is None:
            print("LL is empty")
            return
        elif self.head.value==x:
            self.Head=self.head.next
            return
        else:
            n=self.head
            while n.next:
                if n.next.value==x:
                    break
                n=n.next
            if n.next==None:
                print("elemnt not found")
            else:
                n.next=n.next.next
            
            

ll = LL()
ll.printLL()
print("add BEGIN")
ll.addBegin(30)
ll.addBegin(40)
ll.addBegin(50)
ll.printLL()
print("add END")
ll.addEnd(5)
ll.addEnd(6)
ll.addEnd(7)
ll.printLL()
print("add AFTER")
ll.addAfter(999,30)
ll.addAfter(111,999)
ll.printLL()
print("add BEFORE")
ll.addBefore(999,50)
ll.addBefore(111,57)
ll.printLL()
print("del START")
ll.delStart()
ll.printLL()
print("del END")
ll.delEnd()
ll.printLL()
print("del ANY")
ll.delAny(999)
ll.printLL()

#output
# The linked list is empty!
# add BEGIN
# 50 -> 40 -> 30 -> 
# add END
# 50 -> 40 -> 30 -> 5 -> 6 -> 7 -> 
# add AFTER
# 50 -> 40 -> 30 -> 999 -> 111 -> 5 -> 6 -> 7 -> 
# add BEFORE
# 57  value is found
# 999 -> 50 -> 40 -> 30 -> 999 -> 111 -> 5 -> 6 -> 7 -> 
# del START
# 50 -> 40 -> 30 -> 999 -> 111 -> 5 -> 6 -> 7 -> 
# del END
# 50 -> 40 -> 30 -> 999 -> 111 -> 5 -> 6 -> 
# del ANY
# 50 -> 40 -> 30 -> 111 -> 5 -> 6 -> 
