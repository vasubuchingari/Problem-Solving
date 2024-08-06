class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sub_array_sum=[]
        for i in range(len(nums)):
            current_tot=0
            for j in range(i,len(nums)):
                current_tot=current_tot+nums[j]
                sub_array_sum.append(current_tot)
        sub_array_sum.sort()
        res=sub_array_sum[left-1:right]
        tot=sum(res)%MOD
        return tot
