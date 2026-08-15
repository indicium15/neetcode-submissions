from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                dump = heappop(heap)
        return heap[0]
        