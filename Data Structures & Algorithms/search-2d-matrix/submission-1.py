class Solution:
    def binarySearch(self, row, low, high, target):
        if high >= low:
            middle = low + (high - low) // 2
            if row[middle] == target:
                return True
            # Move Left
            elif row[middle] > target:
                return self.binarySearch(row, low, middle-1, target)
            # Move Right
            elif row[middle] < target:
                return self.binarySearch(row, middle+1, high, target)
        else:
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            low = row[0]
            high = row[-1]
            length = len(row) - 1
            if target >= low and target <=high:
                return self.binarySearch(row, 0, length, target)
            else:
                continue
        return False
        