class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        hash_table = {}
      
        for i, num in enumerate(sorted_nums):
            if num not in hash_table:  
                hash_table[num] = i
        result=[hash_table[x] for x in nums]

        return result
