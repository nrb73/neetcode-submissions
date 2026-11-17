class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAna = {}

        for s in strs:

            k = "".join(sorted(s))

            if k not in groupAna:
                groupAna[k] = []

            groupAna[k].append(s)

        return (list(groupAna.values()))