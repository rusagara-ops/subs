class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows-1
        targetrow = -1

        while top <= bottom:
            mid = (top + bottom)//2
            if target < matrix[mid][0]:
                bottom = mid -1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                targetrow = mid
                break

        if targetrow == -1:
            return False
        l = 0
        r = cols-1

        while l < r:
            mid = (l+r)//2
            if target < matrix[targetrow][mid]:
                r = mid - 1
            elif target > matrix[targetrow][mid]:
                l = mid + 1
            else:
                return True
        return False


        

        
