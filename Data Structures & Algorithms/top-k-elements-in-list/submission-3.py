from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # Sort this counter by the values
        # Descending order 
        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        # Convert to list
        res = list(sorted_counter.keys())
        return res[:k]