class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0]*len(height), [0]*len(height)

        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            maxRight[len(height)-1-i] = max(maxRight[len(height)-i], height[len(height)-i])

        maxWater = 0 

        for i in range(len(height)):
            tempSum = min(maxLeft[i],maxRight[i])-height[i]
            maxWater += max(0,tempSum)
        print(maxWater)
        return maxWater