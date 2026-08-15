from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # the top of the min heap 
        # has the smallest max value of the top k
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                dump = heappop(heap)
        return heap[0]
        