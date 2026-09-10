class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        maxArea = 0
        
        def dfs(i,j):
            nonlocal area

            if(i < 0 or i == len(grid) or j<0 or j == len(grid[0]) or 
                (i,j) in visit or grid[i][j] == 0):
                return

            area += 1

            visit.add((i,j))
            dfs(i-1,j) or dfs(i+1,j) or dfs(i,j-1) or dfs(i,j+1)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visit or grid[i][j] == 0:
                    continue
                area = 0
                dfs(i,j)
                maxArea = max(area, maxArea)
        
        return maxArea