class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        infVal = 2**31 - 1

        queue = collections.deque()
        visit = set()
        level = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visit.add((i,j))

        while queue:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                for x,y in [(a+1,b),(a,b+1),(a-1,b),(a,b-1)]:
                    if (x<0 or x == len(grid) or y < 0 or y == len(grid[0]) or (x,y) in visit
                       or grid[x][y] == -1):
                        continue

                    grid[x][y] = level
                    queue.append((x,y))
                    visit.add((x,y))
            
            level += 1
        
        print(grid)


