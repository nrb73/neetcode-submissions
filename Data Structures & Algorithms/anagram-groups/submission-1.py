class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAnagrams = {}

        for s in strs:

            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)

            if key not in groupAnagrams:
                groupAnagrams[key] = []
            groupAnagrams[key].append(s)

        return (list(groupAnagrams.values()))
