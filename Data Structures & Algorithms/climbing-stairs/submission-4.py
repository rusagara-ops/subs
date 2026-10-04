class Solution:
    def climbStairs(self, n: int) -> int:
        # if n is less or equal to the base cases, the 1 and 2 steps, then we return n
        # build our dp table and fill the basecases like this below
        # we check the basecases to return 1 since for n = 1, or n = 2, we always have to return 1 way
        # and then fill it with ways from 3 to n + 1 and return that

        
        if n <= 2:
            return n
        
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for step in range(3, n+1):
            dp[step] = dp[step-1] + dp[step-2]

        return dp[-1]

