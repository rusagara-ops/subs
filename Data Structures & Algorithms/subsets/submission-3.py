class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def dfs(i):

            #basecase, when the inde exceeds the given nums (alwyas append a copy)
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            #decisions:
            #1. include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #2.remove the previosuly added
            subset.pop()

            #3 not include nums[i]
            dfs(i+1)

        dfs(0)
        return result


            