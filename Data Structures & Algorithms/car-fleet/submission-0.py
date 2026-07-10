class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        timeDict = {}

        for i in range(len(position)):
            timeDict[position[i]] = float((target - position[i])/speed[i])
        
        position.sort(reverse=True)

        for pos in position:
            if stack and stack[-1] >= timeDict[pos]:
                continue
            
            stack.append(timeDict[pos])
        
        return len(stack)