class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    return l


# 2nd solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         di={}
#         for i,x in enumerate(nums):
#             n2=target-x
#             if n2 in di:
#                 return (di[n2],i)
#             elif x not in di:
#                 di[x]=i
            

