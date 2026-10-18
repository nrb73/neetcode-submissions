class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        maxArea = 0
        area = 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def dfs(r, c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return
            
            visited.add((r, c))
            nonlocal area 
            area += 1

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    maxArea = max(maxArea, area)
                    area = 0
        
        return maxArea
            





        
        