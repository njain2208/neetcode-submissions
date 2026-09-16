class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = collections.deque()
        visit = set()
        numFreshFruits = 0
        time = 0
    

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFreshFruits += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
        
        while queue:
            for _ in range(len(queue)):
                a,b = queue.popleft()

                for (x,y) in [(a+1,b),(a,b+1),(a-1,b),(a,b-1)]:
                    if (x<0 or x == len(grid) or y<0 or y == len(grid[0])
                        or (x,y) in visit or grid[x][y] == 0 or grid[x][y] == 2):
                        continue
                    
                    grid[x][y] = 2
                    numFreshFruits -= 1
                    queue.append((x,y))
                    visit.add((x,y))
            
            time += 1
        return max(time-1,0) if numFreshFruits <= 0 else -1
