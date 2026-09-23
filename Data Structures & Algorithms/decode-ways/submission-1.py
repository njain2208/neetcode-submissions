class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}

        def dfs(i,prev):
            nonlocal dp
            if i == len(s):
                if  prev == "":
                    return 1
                else:
                    return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            if ((s[i] == "0" and prev == "") or int(prev+s[i]) > 26):
                return 0
            
            numWays = 0
            
            numWays += dfs(i+1,"")

            if prev == "":
                numWays += dfs(i+1,s[i])
            dp[(i,prev)] = numWays
            
            return numWays
        
        return dfs(0,"")
            

        