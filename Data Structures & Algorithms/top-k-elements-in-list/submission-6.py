class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, f in counts.items():
            freq[f].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for value in freq[i]:
                res.append(value)
                if len(res) == k:
                    return res

