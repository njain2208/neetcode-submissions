class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}

        def dfs(i):
            nonlocal dp
            
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
                
            if i in dp:
                return dp[i]
            
            numWays = dfs(i+1)

            if(i+1 < len(s) and ((s[i] == "1") or (s[i] == "2" and int(s[i+1]) < 7))):
                numWays +=  dfs(i+2)
            
            dp[i] = numWays
            
            return  dp[i]
        
        return dfs(0)
            

        