class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = head
        res = 0
        while n is not None:
            res = res * 2 + n.val
            n = n.next
        return res
