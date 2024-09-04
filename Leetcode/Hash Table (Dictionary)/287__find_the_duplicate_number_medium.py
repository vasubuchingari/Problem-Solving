from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di=Counter(nums)
        for key, value in di.items():
            if value>1:
                return key
            
