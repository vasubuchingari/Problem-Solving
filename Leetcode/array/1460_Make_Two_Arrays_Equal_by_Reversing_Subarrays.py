class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t=target.sort()
        s=arr.sort()
        if arr==target:
            return True
        else:
            False
        
