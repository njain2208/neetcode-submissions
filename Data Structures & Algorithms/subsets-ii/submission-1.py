class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tempSubSet = []
        ans = []

        def dfs(i):
            nonlocal ans, tempSubSet

            if i == len(nums):
                ans.append(tempSubSet[:])
                return

            tempSubSet.append(nums[i])
            dfs(i+1)
            tempSubSet.pop()

            
            while  i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1)
                
                
        dfs(0)
        return ans
        