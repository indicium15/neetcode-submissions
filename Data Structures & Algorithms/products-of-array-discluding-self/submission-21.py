class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # Prefix Array
        current = 1
        prefixes = [1] * len(nums)
        for i in range(len(nums)):
            prefixes[i] = current
            # This keeps it one back
            current *= nums[i]
        current = 1
        for i in range(len(nums)-1, -1, -1):
            prefixes[i] = prefixes[i] * current
            current *= nums[i]
        return prefixes
