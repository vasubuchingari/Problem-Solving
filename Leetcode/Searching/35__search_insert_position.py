# BUBBLE sorting
# LINEAR search & BINARY search 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found=False
        for i in range(len(nums)):
            if nums[i]==target:
                found=True
                break
        if found==True:
            return i
        else:
            nums.append(target)
            for i in range(len(nums)-1):
                for j in range(len(nums)-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            print(nums)
            low=0
            high=len(nums)-1
            while True:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        
