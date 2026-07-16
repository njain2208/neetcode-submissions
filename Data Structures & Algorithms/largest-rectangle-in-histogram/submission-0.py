class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i in range(len(heights)):
            prev_elem_indx = i

            while stack and stack[-1][1]>heights[i]:
                prev_elem_indx, element  = stack.pop()
                area = max(area,(i - prev_elem_indx)*element)
            
            stack.append((prev_elem_indx, heights[i]))

        while stack:
            prev_elem_indx, height = stack.pop()
            
            temp_area = (len(heights)-prev_elem_indx) * height
            area = max(area,temp_area)

        return area
        