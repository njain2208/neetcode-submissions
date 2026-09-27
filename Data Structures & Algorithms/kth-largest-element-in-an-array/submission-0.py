class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ans = []
        
        for i in range(len(nums)):
            if len(ans) == k and ans[0] >nums[i]:
                continue
            heapq.heappush(ans, nums[i])
            if len(ans) > k :
                heapq.heappop(ans)
        
        return ans[0]

