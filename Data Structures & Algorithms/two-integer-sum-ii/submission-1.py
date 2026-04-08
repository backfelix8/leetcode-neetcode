class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = False
        index1 = 0
        index2 = len(numbers) - 1

        while not found:
            if numbers[index1] + numbers[index2] == target and index1 < index2:
                found = True
                return [index1 + 1, index2 + 1]

            elif numbers[index1] + numbers[index2] > target:
                index2 -= 1
            
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1


