class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        dp = {0:1,1:1}

        def dfs(numSteps):
            nonlocal dp

            if numSteps < 0:
                return 0
            
            if numSteps in dp:
                return dp[numSteps] 
            
            dp[numSteps] = dfs(numSteps-2) + dfs(numSteps-1)
            return dp[numSteps]
        
        return dfs(n)
        