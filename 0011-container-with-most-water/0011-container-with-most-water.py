from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. Initialize pointers and max_area variable
        left = 0
        right = len(height) - 1
        max_area = 0

        # 2. Loop until the two pointers meet
        while left < right:
            # Calculate the width of the current container
            width = right - left
            
            # Calculate the height, limited by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate the area of the current container
            current_area = width * current_height
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # 3. Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # 4. Return the maximum area found
        return max_area