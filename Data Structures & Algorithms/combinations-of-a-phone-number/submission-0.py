class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitTOChar = {
            "2": ["a","b","c"],
            "3" :["d","e","f"],
            "4": ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7": ["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        ans =[]

        def dfs(i,comb):
            nonlocal ans
            if i== len(digits):
                if comb =="":
                    return
                ans.append(comb)
                return
            
            for char in digitTOChar[digits[i]]:
                dfs(i+1,comb+char)
        dfs(0,"")
        return ans