#Input: prices = [10,1,5,6,7,1]
#Output: 6

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        maxProfit = 0

        while (r < len(prices)):
            if (prices[r] > prices[l]):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit




        