class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            #if positive number then won't sum to 0
            if nums[i] > 0:
                break
            #check for duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            #two pointer
            while (l < r):

                curSum = nums[l] + nums[r]

                if curSum > target:
                    r -= 1

                elif curSum < target:
                    l += 1

                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res


