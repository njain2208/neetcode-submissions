class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1

        while l<=r:
            m = l +(r-l)//2
            print(l,r, target)

            if nums[m] == target:
                return True
            if nums[l] == nums[m]:
                l += 1
                continue

            if nums[r] == nums[m]:
                r -= 1
                continue

            elif nums[m] < nums[r] or nums[m]< nums[l]:
                if not nums[m] < target <= nums[r]:
                    r = m-1
                    
                else:
                    l = m + 1 
                continue
            
            elif nums[l] < nums[m] or nums[m] > nums[r]:
                if not nums[l] <= target < nums[m]:
                    l = m + 1 
                    
                else:
                    r = m-1
                continue
        
        return False