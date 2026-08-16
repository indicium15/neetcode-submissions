class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        prev_end = 0
        removals = 0
        for interval in intervals:
            if prev_end == 0:
                prev_end = interval[1]
            else:
                # No overlap
                if interval[0] >= prev_end:
                    prev_end = max(prev_end, interval[1])
                else:
                    removals += 1
        return removals


        