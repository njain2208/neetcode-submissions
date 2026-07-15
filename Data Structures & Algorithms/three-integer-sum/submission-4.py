class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):
            if i !=0 and i < len(nums) and nums[i-1] == nums[i]:
                continue

            if nums[i] > 0 :
                break

            j, k = i+1, len(nums)-1
            while j<k:
                if j-1 != i and nums[j-1] == nums[j]:
                    j += 1
                    continue

                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i],nums[j], nums[k]])
                    j += 1
                    k-=1
                elif nums[j] + nums[k] < -nums[i]:
                    j+= 1
                else:
                    k -= 1
        return ans

