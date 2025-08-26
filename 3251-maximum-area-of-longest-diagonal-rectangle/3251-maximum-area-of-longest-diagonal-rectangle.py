class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # Step 1: Initialize tracking variables
        max_diagonal_sq = 0
        max_area = 0

        # Step 2: Iterate through each rectangle
        for l, w in dimensions:
            
            # Step 3: Calculate the squared diagonal for the current rectangle
            current_diagonal_sq = l*l + w*w

            # Step 4: Compare and update
            if current_diagonal_sq > max_diagonal_sq:
                # Found a new longest diagonal, so update both values
                max_diagonal_sq = current_diagonal_sq
                max_area = l * w
            elif current_diagonal_sq == max_diagonal_sq:
                # Same diagonal length, so choose the larger area
                max_area = max(max_area, l * w)
        
        # Step 5: Return the final result
        return max_area