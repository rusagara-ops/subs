class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        visited = set()

        def dfs(i):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num in visited:
                    continue
                current.append(num)
                visited.add(num)
                dfs(i+1)
                current.pop()
                visited.remove(num)
        
        dfs(0)

        return result




            