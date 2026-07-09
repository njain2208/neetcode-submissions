class Solution:
    def expand(self, s: str) -> List[str]:
 
        res = []

        curWord = []
        def dfs(i):
            nonlocal curWord, res
            if i == len(s):
                res.append("".join(curWord))
                return
            
            if s[i] != "{":
                curWord.append(s[i])
                dfs(i+1)
                curWord.pop()
            else:
                i += 1
                tempCharArr = []
        
                while s[i] != "}":
                    if s[i]!= ",":
                        tempCharArr.append(s[i])
                    i += 1

                for char in tempCharArr:
                    curWord.append(char)
                    dfs(i+1)
                    curWord.pop()
        dfs(0)
        return res
            
      