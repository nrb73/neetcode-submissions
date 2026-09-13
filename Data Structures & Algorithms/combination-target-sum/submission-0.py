class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        path = []

        def find(i, remaining):

            if remaining == 0:
                result.append(path[:])
                return
            if i >= len(nums) or remaining < 0:
                return
            

            #choice 1 - we stick to checking the current i
            #appended the current i to path, then check
            path.append(nums[i])
            find(i, remaining - nums[i])

            #choice 2 - we remove the number i we added and try i + 1 onwards
            #remove that number
            path.pop()
            find(i + 1, remaining)

        find(0, target)
        return result
        