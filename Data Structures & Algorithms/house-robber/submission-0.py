class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        def robHelp(i):
            
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(robHelp(i + 1), (nums[i] + robHelp(i + 2)))

            return cache[i]

        return robHelp(0)
        