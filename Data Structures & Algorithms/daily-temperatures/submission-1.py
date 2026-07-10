class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque

        stack = []
        ans = []

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1]-i)
            
            stack.append(i)

        return ans[::-1]