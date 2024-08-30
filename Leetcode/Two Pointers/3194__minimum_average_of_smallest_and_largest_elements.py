class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left=0
        right=len(nums)-1
        avg=float('inf')
        while left<=right:
            average=(nums[left]+nums[right])/2
            avg=min(avg,average)
            right=right-1
            left=left+1
        return avg
        
        # nums.sort()
        # avg=[]
        # while nums:
        #     average=(nums[0]+nums[-1])/2
        #     avg.append(average)
        #     nums.pop(0)
        #     nums.pop()
        # avg.sort()
        # return avg[0]
