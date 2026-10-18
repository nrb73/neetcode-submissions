class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        #capturing Os to Ts
        def capture(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)
        
        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)


        #capturing surrounded territories, or O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #reversing the temporary change, or T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
            