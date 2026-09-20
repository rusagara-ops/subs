class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        numberofislands = 0

        def dfs(row,col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if (row,col) in seen:
                return
            if grid[row][col] == '0':
                return

            seen.add((row,col))

            for r,c in ((1,0),(0,1),(-1,0),(0,-1)):
                newrow = row + r
                newcol = col + c
                dfs(newrow,newcol)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in seen:
                    numberofislands += 1
                    dfs(row,col)

        return numberofislands

