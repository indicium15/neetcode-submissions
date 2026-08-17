class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            # Greater than target - we need to reduce the number
            elif numbers[left] + numbers[right] > target:
                right -= 1
            # Lesser than target - we need to increase the number
            elif numbers[left] + numbers[right] < target:
                left += 1 
        
        