class Solution:
    def isPalindrome(self, s: str) -> bool:

        toCompare = ""

        for ch in s:
            if ch.isalnum():
                toCompare += (ch.lower())

        l, r = 0, len(toCompare) - 1

        while l < r:

            if toCompare[l] != toCompare[r]:
                return False

            l += 1
            r -= 1

        return True
        

        