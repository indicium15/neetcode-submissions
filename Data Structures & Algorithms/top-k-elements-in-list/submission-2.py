from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # Counter.most_common returns a nested string of value, count
        # So we use string comprehension to quickly get the last value
        return [c[0] for c in counter.most_common(k)]

        