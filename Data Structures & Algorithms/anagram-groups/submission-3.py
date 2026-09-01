class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAnagrams = {}

        for s in strs:

            sort = "".join(sorted(s))

            if sort not in groupAnagrams:
                groupAnagrams[sort] = []

            groupAnagrams[sort].append(s)
        return(list(groupAnagrams.values()))
