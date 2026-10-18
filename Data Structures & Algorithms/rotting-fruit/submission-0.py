class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        mins = 0
        fresh = 0

        def addFruit(r, c):
            nonlocal fresh
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 0):
                return
            visited.add((r, c))
            q.append((r, c))
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c - 1)
                addFruit(r, c + 1)
            mins += 1

        return mins if fresh == 0 else -1
        