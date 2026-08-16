class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float("inf")

        while l <= r:
            m = l+(r-l)//2

            if nums[l] <= nums[r]:
                return min(res, nums[l])

            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m+1

            else:
                r =  m-1
        return res