# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        carry=0
        dummy=ListNode(0)
        d_dummy=dummy

        while prev or carry:
            value=prev.val if prev else 0
            tot=value+value+carry
            carry=tot//10
            d_dummy.next=ListNode(tot%10)
            d_dummy=d_dummy.next
            if prev:
                prev=prev.next
        k=dummy.next
        before=None
        while k:
            nxt=k.next
            k.next=before
            before=k
            k=nxt

        return before



        
