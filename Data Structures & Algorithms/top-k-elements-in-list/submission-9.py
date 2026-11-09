class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1
        
        arr = []
        for num, cnt in freqs.items():
            arr.append([cnt, num])
        arr.sort()
        arr.reverse()

        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res