class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits == "":
            return []

        res = []
        sub = []

        def backtrack(i):

            if i >= len(digits):
                res.append("".join(sub))
                return

            for ch in digitToChar[digits[i]]:
                sub.append(ch)
                backtrack(i + 1)
                sub.pop()

        backtrack(0)
        return res

            


        