class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dp = {}

        for num in arr:
            if num in dp:
                dp[num] += 1
                continue
            dp[num] = 1

        luckyInt = -1

        for key in sorted(dp.keys()):
            if key == dp[key]:
                luckyInt = key
        
        return luckyInt