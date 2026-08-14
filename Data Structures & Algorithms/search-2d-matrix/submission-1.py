class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix)-1
        i, j = -1, -1
        
        while l <= r:
            m = l+(r-l)//2

            if matrix[m][0]<= target <= matrix[m][-1]:
                i = m
                break
            
            if target < matrix[m][0]:
                r = m-1
            else:
                l = m+1
        
        if i == -1:
            return False
        
        l , r = 0, len(matrix[i])-1

        while l <= r:
            m = l +(r-l) //2

            if matrix[i][m] == target:
                j = m
                break
            
            if target < matrix[i][m]:
                r = m-1
            else:
                l = m+1
        
        return True if j !=-1 else False
        

