class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        num1 = -1
        count1 = 0

        num2 = -1
        count2 = 0

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
          
        count1 = count2 = 0
        print(num1, num2)

        for i in range(numLen):
            if nums[i] == num1:
                count1 += 1
            elif nums[i] == num2:
                count2 += 1
        
        ans = []
        if count1 > numLen/3:
            ans.append(num1)
        if count2 > numLen/3:
            ans.append(num2)
            
        return ans