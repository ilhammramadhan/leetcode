from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Handle empty matrix case
        if not mat or not mat[0]:
            return []

        # 1. Initialization
        m = len(mat)
        n = len(mat[0])
        result = []
        row, col = 0, 0
        direction_is_up = True # True for up-right, False for down-left

        # 2. The Main Loop
        # The loop will run m * n times to visit every element
        while len(result) < m * n:
            # Add the current element to the result list
            result.append(mat[row][col])

            # 3. Calculate the Next Move
            if direction_is_up:
                # Standard move is row-1, col+1
                # Check for boundary conditions and change direction if needed
                if col == n - 1: # Hit the right wall
                    row += 1
                    direction_is_up = False
                elif row == 0:   # Hit the top wall
                    col += 1
                    direction_is_up = False
                else:            # No walls hit, move up-right
                    row -= 1
                    col += 1
            else: # Moving down-left
                # Standard move is row+1, col-1
                # Check for boundary conditions and change direction if needed
                if row == m - 1: # Hit the bottom wall
                    col += 1
                    direction_is_up = True
                elif col == 0:   # Hit the left wall
                    row += 1
                    direction_is_up = True
                else:            # No walls hit, move down-left
                    row += 1
                    col -= 1
        
        return result