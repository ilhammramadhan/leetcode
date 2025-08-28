from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Sorts the diagonals of a square matrix based on specified rules.
        """
        n = len(grid)
        
        # Step 1: Group elements by their diagonal identifier (r - c).
        # defaultdict(list) conveniently creates an empty list for new keys.
        diagonals = defaultdict(list)
        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])
        
        # Step 2: Sort each diagonal according to the rules.
        for key in diagonals:
            if key >= 0:
                # Bottom-left triangle diagonals (including main) are sorted descending.
                diagonals[key].sort(reverse=True)
            else:
                # Top-right triangle diagonals are sorted ascending.
                diagonals[key].sort()
        
        # Step 3: Rebuild the matrix with the sorted values.
        # We iterate in the same order as the initial traversal to ensure correct placement.
        for r in range(n):
            for c in range(n):
                # Take the first element from the correctly sorted list and place it back.
                grid[r][c] = diagonals[r - c].pop(0)
                
        return grid