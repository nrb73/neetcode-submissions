class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()


        def squareSum(num):

            sum = 0
            while num > 0:

                digit = num % 10
                sum = sum + (digit * digit)
                num = int(num/10)
            return sum

        finalSum = squareSum(n)
        check = False

        while not check:
            if finalSum == 1:
                return True
            if finalSum in seen:
                check = True
            seen.add(finalSum)
            finalSum = squareSum(finalSum)

        return False


        