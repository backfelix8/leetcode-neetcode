class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in diffs:
                return [diffs[diff] + 1, i + 1]
            else:
                diffs[numbers[i]] = i