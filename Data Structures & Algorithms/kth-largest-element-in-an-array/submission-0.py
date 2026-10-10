class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = []
        heapq.heapify(res)
        nums.sort(reverse=True)

        for n in nums:
            heapq.heappush(res, n)
            if len(res) == k:
                return (heapq.heappop(res))

        


        