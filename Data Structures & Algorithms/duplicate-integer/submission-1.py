class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hm = {}

        for n in nums:

            if n in hm:
                return True
            else:
                hm[n] = 1
        
        return False