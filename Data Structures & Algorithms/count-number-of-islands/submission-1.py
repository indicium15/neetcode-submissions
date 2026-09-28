class Solution:
    
    def dfs(self, i, j, grid, visited):
        # We do the bounds check here
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != "1" or (i,j) in visited:
            return
        # visited check here stops circular navigation
        visited.add((i,j))
        # So we can add invalid bounds here
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(i + di, j + dj, grid, visited)

    def numIslands(self, grid):
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # visited check here stops double counting
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.dfs(i, j, grid, visited)
                    count += 1
        return count