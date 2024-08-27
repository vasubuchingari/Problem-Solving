#descending insertion sorting
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        for i in range(1,len(nums)):
            current_value=nums[i]
            position=i
            while current_value>nums[position-1] and position>0:
                nums[position]=nums[position-1]
                position=position-1
            nums[position]=current_value

        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]     
