class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {0:0}
        coins.sort()

        for i in range(1,amount+1):
            dp[i] = float("inf")
            for coin in coins:
                if i-coin<0:
                    break

                dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[amount] if dp[amount] != float("inf") else -1