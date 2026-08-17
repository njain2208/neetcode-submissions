class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1, nums2 = (nums1,nums2) if len(nums1) <= len(nums2) else (nums2,nums1)

        totalLen = len(nums1) +len(nums2)

        mid = (len(nums1)+len(nums2))//2

        l , r = 0, len(nums1)-1

        while True:
            
            i = l +(r-l)//2
            j = mid -i -2

            nums1Left = nums1[i] if 0 <= i < len(nums1) else float("-inf")
            nums1Right = nums1[i+1] if 0 <= (i+1) < len(nums1) else float("inf")

            nums2Left = nums2[j] if 0 <= j < len(nums2) else float("-inf")
            nums2Right = nums2[j+1] if 0 <= (j+1) < len(nums2) else float("inf")

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if totalLen%2 == 0:
                    return (max(nums1Left,nums2Left)+min(nums1Right, nums2Right))/2
                return min(nums1Right, nums2Right)
            
            if nums1Left > nums2Right:
                r = i-1
            else:
                l = i+1
