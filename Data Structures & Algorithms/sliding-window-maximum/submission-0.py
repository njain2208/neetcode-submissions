class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        maxHeap = deque()
        ans = []
        
        for j in range(len(nums)):
            while maxHeap and nums[maxHeap[0]] < nums[j]:
                maxHeap.popleft()
            
            maxHeap.appendleft(j)

            if j >= k-1:
                while maxHeap and maxHeap[-1] <= j-k:
                    maxHeap.pop()
                
                ans.append(nums[maxHeap[-1]])
        
        return ans
