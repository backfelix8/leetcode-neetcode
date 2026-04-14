class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)     # rows
        m = len(matrix[0])  # columns

        top = 0
        bottom = n - 1
        row = 0
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][m - 1]:
                top = row + 1
            elif target >= matrix[row][0] and target <= matrix[row][m - 1]:
                break

        left, right = 0, m - 1
        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif target > matrix[row][col]:
                left = col + 1
            elif target == matrix[row][col]:
                return True

        return False


