class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        sum = numbers[l] + numbers[r]
        
        while sum != target:
            if sum < target:
                l += 1
            if sum > target:
                r -= 1
            sum = numbers[l] + numbers[r] 
        
        return [l + 1, r + 1]