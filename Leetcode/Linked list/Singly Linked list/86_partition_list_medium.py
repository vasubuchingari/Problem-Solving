# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great_dummy=ListNode(0)
        less_dummy=ListNode(0)
        great=great_dummy
        less=less_dummy
        current=head
        while current:
            if current.val<x:
                less.next=current
                less=less.next
            else:
                great.next=current
                great=great.next
            current=current.next
        great.next=None
        less.next=great_dummy.next
        return less_dummy.next
    
