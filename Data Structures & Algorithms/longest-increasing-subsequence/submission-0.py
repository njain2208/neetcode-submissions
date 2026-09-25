class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [-1]*len(nums)

        def dfs(i):
            nonlocal dp
            if dp[i] != -1:
                return dp[i]
            
            temp = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    temp = max(temp, 1 + dfs(j))
            dp[i] = temp
            return dp[i]

        for i in range(0,len(nums)):
            dfs(i)
        
        return max(dp)