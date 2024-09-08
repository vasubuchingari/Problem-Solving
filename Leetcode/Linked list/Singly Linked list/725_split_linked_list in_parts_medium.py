# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        n = head
        while n:
            length += 1
            n = n.next
        
        part_size = length // k
        remainder = length % k
        
        l = []
        current = head
        
        for i in range(k):
            part_head = current  # Head of the current part
            size = part_size + (1 if i < remainder else 0)  # Calculate the size of this part
            
            # Traverse the current part
            for j in range(size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next  # Store the start of the next part
                current.next = None  # Break the list
                current = next_part  # Move to the next part
            
            # Append the head of the current part to the result list
            l.append(part_head)
        
        # If there are fewer nodes than parts, append None for the remaining parts
        while len(l) < k:
            l.append(None)
        
        return l
