from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check all 4 possible rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            # Step 1: Check if the current matrix matches the target
            if mat == target:
                return True
            
            # Step 2: Rotate the matrix 90 degrees clockwise
            # mat[::-1] flips the matrix upside down
            # zip(*...) transposes the matrix
            mat = [list(row) for row in zip(*mat[::-1])]
            
        # If we check all 4 rotations and none match, it's impossible
        return False