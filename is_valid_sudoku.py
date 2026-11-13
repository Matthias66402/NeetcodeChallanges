class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                box = (i // 3) * 3 + j // 3
                if value in rows[i] or value in cols[j] or value in boxes[box]:
                    return False
                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)
        return True


        valid_values = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] not in valid_values):
                    return False
        return True


board_true =  [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


board_false = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


is_valid_sudoku = Solution().isValidSudoku(board_true)
print(f"is valid: {is_valid_sudoku}")

