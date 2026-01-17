class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Compare every unique pair of rectangles (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # 1. Determine the boundaries of the intersection
                inter_bottom_x = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bottom_y = max(bottomLeft[i][1], bottomLeft[j][1])
                inter_top_x = min(topRight[i][0], topRight[j][0])
                inter_top_y = min(topRight[i][1], topRight[j][1])
                
                # 2. Calculate dimensions of the intersection
                width = inter_top_x - inter_bottom_x
                height = inter_top_y - inter_bottom_y
                
                # 3. Check if an intersection actually exists
                if width > 0 and height > 0:
                    # The largest square in a rectangle is limited by its smallest side
                    side = min(width, height)
                    max_side = max(max_side, side)
        
        # 4. Return the area
        return max_side * max_side