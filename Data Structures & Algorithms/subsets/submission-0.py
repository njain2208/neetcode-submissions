class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        tempSubset = []

        def dfs(i):
            nonlocal ans, tempSubset
            if i >= len(nums):
                ans.append(tempSubset[:])
                return

            dfs(i+1)

            tempSubset.append(nums[i])

            dfs(i+1)
            tempSubset.pop()

        dfs(0)
        return ans
        