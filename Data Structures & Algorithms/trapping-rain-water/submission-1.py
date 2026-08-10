class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) ==2:
            return 0

        maxLeft, maxRight = 0, 0
        rainWater =0

        l, r = 0, len(height)-1

        while l<=r:
            if maxLeft <= maxRight:
                rainWater += max(0,maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
                continue
            
            rainWater += max(0,maxRight - height[r])
            maxRight = max(maxRight, height[r])
            r -= 1

        return rainWater