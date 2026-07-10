class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for val in tokens:
            if val == "+":
                x = stack.pop()
                y = stack.pop()
                val = x+y
            elif val == "*":
                x = stack.pop()
                y = stack.pop()
                val = x*y
            elif val == "-":
                x = stack.pop()
                y = stack.pop()
                val = y-x
            elif val == "/":
                x = stack.pop()
                y = stack.pop()
                val = y/x
            stack.append(int(val))
            
        return stack[0]
        