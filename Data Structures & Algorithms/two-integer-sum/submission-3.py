class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}

        for i, n in enumerate(nums):
            candidates[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            candidate = candidates.get(diff)
            if candidate != None and candidate != i:
                return [i, candidate]

            candidates[diff] = i
        