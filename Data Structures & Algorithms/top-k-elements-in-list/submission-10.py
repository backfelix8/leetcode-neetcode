class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        heap = []
        for i in freqs.keys():
            heapq.heappush(heap, (freqs[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res