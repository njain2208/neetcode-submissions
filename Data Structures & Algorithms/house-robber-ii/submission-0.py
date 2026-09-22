class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=3:
            return max(nums)

        def helperFunction(nums):
            for i in range(len(nums)-3,-1,-1):
                nums[i] = max(nums[i]+nums[i+2],nums[i+1])
                nums[i+1] = max(nums[i+1], nums[i+2])
            return nums[0]

        newArr = nums[1::]


        ans = max(helperFunction(nums[0:len(nums)-1]), helperFunction(newArr))
        return ans



        