class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target = total_area / 2
        
        # Binary search for the y-coordinate
        low = min_y
        high = max_y
        
        # 100 iterations provides precision far beyond 10^-5
        for _ in range(100):
            mid = (low + high) / 2
            area_below = 0
            
            for x, y, l in squares:
                if y + l <= mid:
                    # Square is completely below the line
                    area_below += l * l
                elif y < mid:
                    # Line cuts through the square
                    area_below += (mid - y) * l
                # If y >= mid, the square is entirely above, add nothing
            
            if area_below < target:
                low = mid
            else:
                high = mid
                
        return low