class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sortedS = {}
        sortedT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sortedS[s[i]] = 1 + sortedS.get(s[i], 0)
            sortedT[t[i]] = 1 + sortedT.get(t[i], 0)
        
        if sortedS == sortedT:
            return True
            
        return False
