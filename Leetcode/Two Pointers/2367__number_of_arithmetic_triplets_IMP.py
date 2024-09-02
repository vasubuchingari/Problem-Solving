class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            j=i+1
            k=i+2
            while j<n and k<n:
                if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                    res=res+1
                    break
                elif   nums[j]-nums[i]<diff:
                    j=j+1
                elif nums[k]-nums[j]<diff:
                    k=k+1
                else:
                    break    
        return res  
