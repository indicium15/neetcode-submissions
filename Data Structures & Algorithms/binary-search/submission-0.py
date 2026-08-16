class Solution:
    def binarySearch(self, nums, low, high, key):
        if high >= low:
            mid = low + (high - low) // 2
            if key > nums[mid]:
                return self.binarySearch(nums, mid + 1, high, key)
            elif key < nums[mid]:
                return self.binarySearch(nums, low, mid -1, key)
            elif key == nums[mid]:
                return mid
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
        
        