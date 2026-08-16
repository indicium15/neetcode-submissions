class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # Sort intervals by starting point
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # Start value of new interval
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            # Start value of previous interval
            previous_start = res[-1][0]
            previous_end = res[-1][1]
            # If the starting point of the new interval is less than the previous
            if interval_start <= previous_end:
                # Update the result array end with the greater value
                res[-1][1] = max(interval_end, previous_end)

            else:
                # This is a unique interval
                res.append(intervals[i])

        return res