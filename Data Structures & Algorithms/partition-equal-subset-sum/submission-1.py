class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        goal = sum(nums)/2

        nums.sort()
        dp = {}
        def dfs(i,rmndr):
            if  i == len(nums) or nums[i] > rmndr :
                return False
            if (i, rmndr) in dp:
                return dp[(i, rmndr)]
            if nums[i] == rmndr:
                return True
            
            dp[(i,rmndr)] =  dfs(i+1,rmndr-nums[i]) or dfs(i+1,rmndr)
            return dp[(i,rmndr)]
        
        return dfs(0,int(goal))