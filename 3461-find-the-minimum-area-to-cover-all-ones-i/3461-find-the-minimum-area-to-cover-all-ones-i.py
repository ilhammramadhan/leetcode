from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Step 1 & 2: Initialize boundary variables
        # Initialize min values to be larger than any possible index
        # and max values to be smaller than any possible index.
        min_row, min_col = rows, cols
        max_row, max_col = -1, -1
        
        # Iterate through the grid to find the boundaries of all 1s
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Update the boundaries if a '1' is found
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        
        # Step 3: Calculate the height and width of the bounding rectangle
        # We add 1 because the boundary indices are inclusive.
        # For example, a rectangle from col 0 to col 2 has a width of 2 - 0 + 1 = 3.
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        
        # Step 4: Calculate and return the area
        return height * width