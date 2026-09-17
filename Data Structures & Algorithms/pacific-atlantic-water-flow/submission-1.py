class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pcficSet = set()
        atlntcSet = set()

        def dfs(i,j, prevHeight, isAtlantic):
            nonlocal pcficSet, atlntcSet

            if (i< 0 or i>= len(heights) or j < 0 or j >= len(heights[0]) or heights[i][j] < prevHeight):
                return
            
            if isAtlantic:
                if (i,j) in atlntcSet:
                    return
                atlntcSet.add((i,j))
            else:
                if (i,j) in pcficSet:
                    return
                pcficSet.add((i,j))
            
            dfs(i-1, j, heights[i][j], isAtlantic)
            dfs(i+1, j, heights[i][j], isAtlantic)
            dfs(i, j-1, heights[i][j], isAtlantic)
            dfs(i, j+1, heights[i][j], isAtlantic)
        
        for i in range(len(heights)):
            dfs(i,0,-1,False)

            dfs(i,len(heights[0])-1,-1,True)
        
        for j in range(len(heights[0])):
            dfs(0,j,-1,False)

            dfs(len(heights)-1,j,-1,True)
        
        print(pcficSet, atlntcSet)
            
        ans = []

        for node in pcficSet:
            if node in atlntcSet:
                ans.append(node)
        return ans