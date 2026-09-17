class Solution:
    def solve(self, board: List[List[str]]) -> None:

        queue = collections.deque([])

        for i in range(len(board)):
            if board[i][0] == "O":
                queue.append((i, 0))
            
            if board[i][len(board[0])-1] == "O":
                queue.append((i, len(board[0])-1))

        for j in range(len(board[0])):
            if board[0][j] == "O":
                queue.append((0, j))
            
            if board[len(board)-1][j] == "O":
                queue.append((len(board)-1, j))

        visit = set()

        def dfs(i,j):
            nonlocal visit
            if(i<0 or i>= len(board) or j<0 or j>= len(board[0]) or 
                (i,j) in visit or board[i][j] == "X"):
                return
            
            visit.add((i,j))
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        
        for (a,b) in queue:
            dfs(a,b)
        print(queue, visit)

        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == "O" and (i,j) not in visit:

                    board[i][j] = "X"
                
        