class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        layer_1 = []

        while left <= right:
            index = (left + right) // 2
            hit = matrix[index]

            if hit[0] <= target and hit[-1] >= target:
                layer_1 = hit
                break
            elif hit[0] < target:
                left = index + 1
            elif hit[-1] > target:
                right = index - 1
        
        if not layer_1:
            return False
        
        left = 0
        right = len(layer_1) - 1

        while left <= right:
            index = (left + right) // 2
            hit = layer_1[index]

            if hit == target:
                return True
            elif hit < target:
                left = index + 1
            elif hit > target:
                right = index -1
        
        return False