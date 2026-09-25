class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = 1
        maxProduct = 1

        ans = float("-inf")

        for i in range(len(nums)):
            temp = maxProduct
            maxProduct = max(minProduct*nums[i], maxProduct*nums[i], nums[i])
            minProduct = min(minProduct*nums[i], temp*nums[i], nums[i])
            ans = max(ans, maxProduct)
        return ans


        