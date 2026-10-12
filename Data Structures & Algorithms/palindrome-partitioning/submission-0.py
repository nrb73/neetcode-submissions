class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []

        def isValid(st):
            l = 0
            r = len(st) - 1

            while (l < r):
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True


        def dfs(i):

            if i >= len(s):
                res.append(subset[:])
                return

            for j in range(i, len(s)):
                if isValid(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j + 1)
                    subset.pop()

        dfs(0)
        return res

        
        