class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        sArr = list(s)

        for char in sArr:
            if stack and ((char == ")" and stack[-1] == "(") or 
                (char == "}" and stack[-1] == "{") or  
                (char == "]" and stack[-1] == "[")):
                stack.pop()
                print("here",stack)
                continue
            
            stack.append(char)
            print(stack)
        
        return True if len(stack) == 0 else False