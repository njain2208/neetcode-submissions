class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        sum = 0
        combination = {}
        ans = []

        def dfs(i):
            nonlocal sum, combination, ans
            if sum >= target:
                if sum == target:
                    combi = []
                    for key in combination.keys():
                        combi.extend([key]*combination[key])
                    
                    ans.append(combi)
                return

            if i >= len(nums):
                return

            combination[nums[i]] = combination.get(nums[i],0) + 1
            sum += nums[i]

            dfs(i)

            combination[nums[i]] -= 1
            if combination[nums[i]] == 0:
                del combination[nums[i]]

            sum -= nums[i]

            dfs(i+1)
        
        dfs(0)
        return ans


        