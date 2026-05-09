from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # A matrix of m x n (where both are even) will have exactly min(m, n) // 2 layers
        layers = min(m, n) // 2
        
        for l in range(layers):
            # Define the boundaries for the current layer
            top, bottom = l, m - 1 - l
            left, right = l, n - 1 - l
            
            # Step 1 & 2: Extract elements in clockwise order
            elements = []
            
            # Top row (left to right, excluding top-right corner)
            for j in range(left, right):
                elements.append(grid[top][j])
            
            # Right column (top to bottom, excluding bottom-right corner)
            for i in range(top, bottom):
                elements.append(grid[i][right])
            
            # Bottom row (right to left, excluding bottom-left corner)
            for j in range(right, left, -1):
                elements.append(grid[bottom][j])
                
            # Left column (bottom to top, excluding top-left corner)
            for i in range(bottom, top, -1):
                elements.append(grid[i][left])
                
            # Step 3: Calculate effective rotations and shift the array
            eff_k = k % len(elements)
            # A left shift in a 1D array equals a counter-clockwise rotation in our 2D grid
            rotated = elements[eff_k:] + elements[:eff_k]
            
            # Step 4: Put the rotated elements back into the grid
            idx = 0
            
            # Top row
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
                
            # Right column
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
                
            # Bottom row
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
                
            # Left column
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid