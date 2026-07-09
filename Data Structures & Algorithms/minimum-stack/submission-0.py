class MinStack:

    def __init__(self):
        self.minStack = []
        self.Stack = []
        
    def push(self, val: int) -> None:
        self.Stack.append(val)
        newVal = min(self.minStack[-1],val) if self.minStack else val
        
        self.minStack.append(newVal)

        

    def pop(self) -> None:
        self.Stack.pop()
        if self.minStack:
            self.minStack.pop()
        
    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
