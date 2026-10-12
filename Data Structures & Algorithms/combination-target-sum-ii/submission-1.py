class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()


        def backtrack(i, curSum):

            if curSum == target:
                res.append(path[:])
                return
            if curSum > target:
                return

            for j in range(i, len(candidates)):
                if (j > i and candidates[j] == candidates[j-1]):
                    continue
                path.append(candidates[j])
                backtrack(j + 1, curSum + candidates[j])
                path.pop()
            
        backtrack(0, 0)
        return res