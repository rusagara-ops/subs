class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def dfs(i):
            if i >= len(s):
                result.append(current.copy())
                return
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word == word[::-1]:
                    current.append(word)
                    dfs(j+1)
                    current.pop()

        dfs(0)
        return result

