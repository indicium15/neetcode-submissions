class Solution:
    def unRotate(self, nums: List[int]) -> List[int]:
        popped = nums.pop()
        nums.insert(0, popped)
        return nums

    def findMin(self, nums: List[int]) -> int:
        # Array was sorted
        # Now rotated
        # What makes it rotated? If the end > start
        # Keep un-rotating until start < end
        # Return nums[0]
        while nums[0] > nums[-1]:
            nums = self.unRotate(nums)
        return nums[0] 