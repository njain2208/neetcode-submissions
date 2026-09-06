class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visit = set() 

        def dfs(i,j, wordIndx):
            if wordIndx == len(word):
                return True

            if i<0 or i >=len(board) or j<0 or j>= len(board[0]) or (i,j) in visit or board[i][j] != word[wordIndx]:
                return False

            visit.add((i,j))

            res = False
            for a,b in [[-1,0],[0,-1],[1,0],[0,1]]:
                if dfs(i+a,j+b, wordIndx+1):
                    visit.remove((i,j))
                    return True
            
            visit.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        
        return False
            

        