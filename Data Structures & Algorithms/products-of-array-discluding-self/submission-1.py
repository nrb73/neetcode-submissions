class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answers = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answers[i] = prefix
            prefix *= nums[i]

        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= suffix
            suffix *= nums[i]

        return answers