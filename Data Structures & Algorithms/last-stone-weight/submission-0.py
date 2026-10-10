class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while (len(heap)) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if (first > second):
                heapq.heappush(heap, -(first - second))
        
        if len(heap) == 1:
            ans = -heapq.heappop(heap)
            return ans
        
        return 0

        