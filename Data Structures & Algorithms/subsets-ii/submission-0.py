class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tempSubSet = []
        ans = []

        def dfs(i):
            nonlocal ans, tempSubSet
            ans.append(tempSubSet[:])
            
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j-1]:
                    continue
                
                tempSubSet.append(nums[j])
                dfs(j+1)
                tempSubSet.pop()
        
        dfs(0)
        return ans
        