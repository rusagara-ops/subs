class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def dfs():
            if len(current) == n*2:
                result.append(''.join(current))
                return

            opening = current.count('(')
            closed = current.count(')')

            if opening < n:
                current.append('(')
                dfs()
                current.pop()

            if closed < opening:
                current.append(')')
                dfs()
                current.pop()

        dfs()
        return result


                
