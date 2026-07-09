class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        m, n = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j,dist):
            nonlocal grid, visit
            if(i<0 or i>=m or j<0 or j>=n
                or (i,j) in visit or grid[i][j] == -1 
                or dist > grid[i][j]):
                return
            
            if grid[i][j] != 0:
                grid[i][j] = dist

            visit.add((i,j))
            for (a,b) in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(i+a,j+b,dist+1)
            visit.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j,0)