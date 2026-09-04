class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        queue = collections.deque(nums)
        
        def dfs(queue):
            if len(queue)  == 1:
                return [list(queue)[:]]

            temp = []
            for _ in range(len(queue)):
                startNum = queue.pop()
                subsetArr = dfs(queue)

                for i in range(len(subsetArr)):
                    subsetArr[i].append(startNum)

                queue.appendleft(startNum)
                temp.extend(subsetArr)
            return temp
        
        return dfs(queue)