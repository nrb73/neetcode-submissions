class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                cur = board[r][c]
                if(cur in rowSet[r] or cur in colSet[c] or cur in squareSet[(r//3, c//3)]):
                    return False

                rowSet[r].add(cur)
                colSet[c].add(cur)
                squareSet[(r//3, c//3)].add(cur)
        return True
        