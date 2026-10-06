class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        targetList = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            targetList[index] += 1


        l = 0
        r = len(s1) - 1


        while (r <= len(s2)):
            
            checkList = [0] * 26
            for char in s2[l: r + 1]:
                index = ord(char) - ord('a')
                checkList[index] += 1

            if checkList == targetList:
                return True
            else:
                l += 1
                r += 1
        return False



        