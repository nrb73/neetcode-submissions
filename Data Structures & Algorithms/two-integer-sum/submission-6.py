class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashDiff = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashDiff:
                return [hashDiff[diff], i]
            hashDiff[n] = i

        


        


        