# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1=None
        while l1:
            nxt1=l1.next
            l1.next=prev1
            prev1=l1
            l1=nxt1
        prev2=None
        while l2:
            nxt2=l2.next
            l2.next=prev2
            prev2=l2
            l2=nxt2
        print(prev1)
        print("\n")
        print(prev2)
        tot=0
        dummy=ListNode(0)
        current=dummy
        carry=0
        while prev1 or prev2 or carry:
            value1=prev1.val if prev1 else 0
            value2=prev2.val if prev2 else 0
            s=value1+value2+carry
            carry=s//10
            current.next=ListNode(s%10)
            current=current.next
            if prev1:
                prev1=prev1.next
            if prev2:
                prev2=prev2.next
        print(dummy.next)
        l3=dummy.next
        prev3=None
        while l3:
            nxt3=l3.next
            l3.next=prev3
            prev3=l3
            l3=nxt3
        return prev3

        

            
        
