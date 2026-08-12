class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc_map = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in loc_map:
                return [loc_map[j], i]
            loc_map[num] = i