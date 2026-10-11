class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        curr = []
        res = []

        def backtrack(closeP, openP):

            if closeP == openP == n:
                res.append("".join(curr))
                return
            if openP < n:
                curr.append("(")
                backtrack(closeP, openP + 1)
                curr.pop()
            if closeP < openP:
                curr.append(")")
                backtrack(closeP + 1, openP)
                curr.pop()

        backtrack(0,0)
        return res
        