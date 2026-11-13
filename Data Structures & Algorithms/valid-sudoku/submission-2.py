class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_array = [0] * 9

        # rows
        for i in range(9):
            check_array = [0] * 9
            for j in range(9):
                if board[i][j] != ".":
                    if check_array[int(board[i][j]) - 1] > 0:
                        return False
                    check_array[int(board[i][j]) - 1] += 1

        
        # columns
        for i in range(9):
            check_array = [0] * 9
            for j in range(9):
                if board[j][i] != ".":
                    if check_array[int(board[j][i]) - 1] > 0:
                        return False
                    check_array[int(board[j][i]) - 1] += 1

        # fields
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
                
        
        return True
        