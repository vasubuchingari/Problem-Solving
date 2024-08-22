from collections import Counter
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1)
        c2=Counter(nums2)
        res=[]
        count1=0
        for x in nums1:
            if c2[x]:
                count1=count1+1
        res.append(count1)
        count2=0
        for x in nums2:
            if c1[x]:
                count2=count2+1
        res.append(count2)

        return res

        
