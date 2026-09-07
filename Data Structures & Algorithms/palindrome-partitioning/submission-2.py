class Solution:
    def isPalindrome(self, arr: str):
        i, j = 0, len(arr) -1
        while i<=j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        subString = []

        def dfs(i):
            nonlocal ans, subString
            if i>= len(s):
                ans.append(subString[::])
                return 
            
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if self.isPalindrome(substr):
                    subString.append(substr)
                    dfs(j+1)
                    subString.pop()
        
        dfs(0)

        return ans

        