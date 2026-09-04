class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        sortedNums = sorted(counts.items(), key = lambda x : x[1], reverse = True)

        res = []
        for i in range(k):
            toAppend, _ = sortedNums[i]
            res.append(toAppend)
        
        return (res)