from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Insertion sorting
        for i in range(1, len(nums)):
            current_element = nums[i]
            position = i
            while position > 0 and current_element < nums[position - 1]:
                nums[position] = nums[position - 1]
                position = position - 1
            nums[position] = current_element

        # Binary search to find all occurrences
        l = []
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                # Find the first occurrence
                first = mid
                while first >= 0 and nums[first] == target:
                    first -= 1
                first += 1

                # Find the last occurrence
                last = mid
                while last < len(nums) and nums[last] == target:
                    last += 1
                last -= 1

                # Append all indices of target
                l.extend(range(first, last + 1))
                break
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return l

