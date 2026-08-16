class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # Start value of second interval
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            previous_start = res[-1][0]
            previous_end = res[-1][1]
            if interval_start <= previous_end:
                res[-1][1] = max(interval_end, previous_end)
            else:
                res.append(intervals[i])

        return res