class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        extended_nums=nums+nums
        ones_count=nums.count(1)
        # print(extended_nums,ones_count)
        inital_window=extended_nums[0:ones_count]
        min_swaps=inital_window.count(0)
        current_swaps=min_swaps
        for i in range(1,n):
            if extended_nums[i-1]==0:
                current_swaps=current_swaps-1
            if extended_nums[i+ones_count-1]==0:
                current_swaps=current_swaps+1
            min_swaps=min(min_swaps,current_swaps)
        return min_swaps
