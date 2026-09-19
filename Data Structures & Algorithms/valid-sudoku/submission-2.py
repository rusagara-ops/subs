class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seenrows = set()
        seencols = set()
        seensquare = set()

        for row in range(ROWS):
            for col in range(COLS):
                square= (row//3, col//3)
                # if not board[row][col].isalnum():
                #     continue

                if board[row][col] in seenrows or board[row][col] in seencols or (square,board[row][col]) in seensquare:
                    return False
                else:
                    seenrows.add((row,board[row][col]))
                    seencols.add((col,board[row][col]))
                    seensquare.add((square,board[row][col]))

        return True
