class Solution:
    
    def dfs(self, i,j, grid, visited):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or (i,j) in visited or grid[i][j] != 1:
            return 0
        visited.add((i,j))
        # When you recurse, just keep adding 1 to the sum to track the length as well
        # Do not need to pass length as another parameter in the function
        return 1 + sum(self.dfs(i+di, j+dj, grid, visited) for di, dj in [(1,0),(-1,0),(0,1),(0,-1)])
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_length = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # remember to check valid before starting dfs
                if grid[i][j] == 1 and (i,j) not in visited:
                    length = self.dfs(i,j,grid,visited)
                    max_length = max(max_length, length)
        return max_length

        
        