class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_set = set(nums)
        if len(nums) == len(test_set):
            return False
        else:
            return True      