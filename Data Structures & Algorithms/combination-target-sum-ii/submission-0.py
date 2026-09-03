class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        tempQueue = []
        remaining = target
        ans = []

        candidates.sort()

        def dfs(i):
            nonlocal remaining, tempQueue, ans
            if remaining == 0:
                ans.append(tempQueue[:])
                return 
            if i == len(candidates):
                return

            for j in range(i, len(candidates)):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                
                if candidates[j] > remaining:
                    break

                tempQueue.append(candidates[j])
                remaining -= candidates[j]

                dfs(j+1)
                remaining += candidates[j]
                tempQueue.pop()
        dfs(0)
        return ans
                