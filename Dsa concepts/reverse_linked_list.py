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
        
    def reverseLL(self):
        n=self.head
        prev=None
        while n:
            nxt=n.next
            n.next=prev
            prev=n
            n=nxt
            
        self.head=prev
               
ll = LL()
ll.printLL()
print("add BEGIN")
ll.addBegin(30)
ll.addBegin(40)
ll.addBegin(50)
ll.printLL()
ll.reverseLL()
ll.printLL()

#output
The linked list is empty!
add BEGIN
50 -> 40 -> 30 -> 
30 -> 40 -> 50 -> 
