class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        freqs = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, count in counts.items():
            freqs[count].append(n)

        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res
        