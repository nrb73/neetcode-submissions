class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax * n
            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            result = max(curMax, result)

        return result
        