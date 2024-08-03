# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=head
        while n and n.next is not None:
            if n.val==n.next.val:
                n.next=n.next.next
            else:
                n=n.next
        return head
