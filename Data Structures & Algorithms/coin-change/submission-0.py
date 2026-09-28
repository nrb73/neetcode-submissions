class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def dp(amount):

            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]

            result = float("inf") #just a max value

            for coin in coins:
                if(amount - coin) >= 0:
                    result = min(result, 1 + dp(amount - coin))

            cache[amount] = result

            return (cache[amount])

        
        minCoins = dp(amount)

        if minCoins == float("inf"):
            return -1

        return minCoins

        
        