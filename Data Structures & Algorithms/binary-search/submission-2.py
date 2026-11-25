class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            hit = nums[index]

            if hit == target:
                return index
            elif hit > target:
                right = index - 1
            elif hit < target:
                left = index + 1
        
        return -1
