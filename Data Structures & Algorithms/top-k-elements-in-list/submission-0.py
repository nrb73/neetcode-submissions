class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        sorted_count = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))

        i = 0
        output = []
        for (num, count) in sorted_count.items():

            if i == k:
                break
            output.append(num)
            i = i + 1
        return output