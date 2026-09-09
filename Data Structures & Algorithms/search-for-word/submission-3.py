class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col,i):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[i] or (row,col) in visited:
                return False

            visited.add((row,col))
            result = (dfs(row+1,col,i+1) or
                    dfs(row,col+1,i+1) or
                    dfs(row-1,col,i+1) or
                    dfs(row,col-1,i+1))
            visited.remove((row,col))

            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0) == True:
                    return True
        return False

        # time = O(n*m for the board times the dfs function which is 4^n(n is the length of the word))


