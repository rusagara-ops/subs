class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def dfs(i):
            if i >= len(s):
                result.append(current.copy())
                return
            for j in range(i, len(s)):
                if self.ispalindrome(s, i, j):
                    current.append(s[i:j+1])
                    dfs(j+1)
                    current.pop()

        dfs(0)
        return result


    def ispalindrome(self,string, l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

