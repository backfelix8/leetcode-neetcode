class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = 0 

        while left < right:
            left_value = heights[left]
            right_value = heights[right]
            area = min(left_value, right_value) * abs(left - right)

            if area > max_area:
                max_area = area
            
            if left_value <= right_value:
                left += 1
            elif left_value > right_value:
                right -= 1

        return max_area
