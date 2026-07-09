class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                number = board[row][col]
                if number in rows[row] or number in cols[col] or number in boxes[row//3][col//3]:
                    return False
                if number != ".":
                    rows[row].add(number)
                    cols[col].add(number)
                    boxes[row//3][col//3].add(number)

        return True
                
    


