class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        jSet = set()
        posDiagonalSet = set()
        negDiagonalSet = set()

        NBoard = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def dfs(num):
            nonlocal jSet, posDiagonalSet, negDiagonalSet
            if num == n:
                temp =[]
                for i in range(n):
                    temp.append("".join(NBoard[i][::]))
                
                ans.append(temp)
                return

            for j in range(n):

                if j in jSet or (num+j) in posDiagonalSet or (num-j) in negDiagonalSet:
                    continue
                NBoard[num][j] = 'Q'
                jSet.add(j)
                negDiagonalSet.add(num-j)
                posDiagonalSet.add(num+j)

                dfs(num+1)

                NBoard[num][j] = '.'
                jSet.remove(j)
                negDiagonalSet.remove(num-j)
                posDiagonalSet.remove(num+j)
        
        dfs(0)
        return ans

        