class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashDiff = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in hashDiff:
                return [hashDiff[diff], i + 1]
            hashDiff[num] = i + 1
        return []

        

        
        