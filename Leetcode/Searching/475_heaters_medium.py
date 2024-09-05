class Solution:
    def binarySearch(self, heaters, house):
        low = 0
        high = len(heaters) - 1
        while low <= high:
            mid = (low + high) // 2
            if heaters[mid] == house:
                return mid
            elif house > heaters[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # If exact match isn't found, `low` will be the position where `house` would be inserted
        return low

    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0
        for house in houses:
            pos = self.binarySearch(heaters, house)

            left_heater_distance = (
                float("inf") if pos == 0 else house - heaters[pos - 1]
            )
            right_heater_distance = (
                float("inf") if pos == len(heaters) else heaters[pos] - house
            )

            closest_distance = min(left_heater_distance, right_heater_distance)
            min_radius = max(min_radius, closest_distance)
        return min_radius
