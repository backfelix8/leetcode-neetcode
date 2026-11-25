class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2
            h_prop = self.simulateEatingSpeed(piles, h, k)
            
            if h_prop > h:
                left = k + 1

            else:
                right = k - 1
        
        return left
    	

    def simulateEatingSpeed(self, piles: List[int], h:int, k:int) -> int:
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k
            
        return hours