class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        minCost = float("inf")
        dp = {}

        def dfs(node):
            nonlocal dp, minCost
            if node > len(cost):
                return float("inf")

            if node == len(cost):
                return 0

            if node in dp:
                return dp[node]

            dp[node] = min(dfs(node+1), dfs(node+2)) + cost[node]
            return dp[node]

        return min(dfs(0),dfs(1))


            
        