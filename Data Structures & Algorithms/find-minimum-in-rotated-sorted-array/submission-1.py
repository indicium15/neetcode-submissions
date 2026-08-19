class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Take mid
        # Compare to end
        # if mid is greater than the end, the minimum is in the second half of the array (mid+1 -> end)
        # if mid is lesser than the end, the minimum is between (start, mid)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
        
