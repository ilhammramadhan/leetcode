from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        # Step 1: Accumulate heights of consecutive 1s column by column
        for i in range(m):
            for j in range(n):
                # If it's a 1 and not the first row, add the height from the row above
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                    
        # Step 2 & 3: Sort each row and calculate the maximum area
        for i in range(m):
            # Sort the current row's heights in descending order
            # We don't sort the original matrix in-place to avoid messing up column alignments 
            # for the logic, though here we've already done the vertical accumulation, 
            # so sorting row by row independently is perfectly safe.
            curr_row = sorted(matrix[i], reverse=True)
            
            # Calculate the maximum area using the current row as the base
            for j in range(n):
                # The height is curr_row[j], the width is j + 1
                current_area = curr_row[j] * (j + 1)
                
                # Update max_area if we found a larger one
                max_area = max(max_area, current_area)
                
        return max_area