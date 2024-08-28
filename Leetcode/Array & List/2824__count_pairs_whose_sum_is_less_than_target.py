class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l=[]
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    l.append((i,j))
        print(l)
        return len(l)
                

        
