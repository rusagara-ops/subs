class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        rows = len(image)
        cols = len(image[0])

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != original or image[row][col] == color:
                return
            image[row][col] = color
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        dfs(sr,sc)
        return image



