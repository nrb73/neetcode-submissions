class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in numSet:

            currNum = n

            if (n - 1) not in numSet:

                length = 1
                while ((currNum + 1) in numSet):
                    length += 1
                    currNum += 1

                longest = max(longest, length)

        return longest

        
        