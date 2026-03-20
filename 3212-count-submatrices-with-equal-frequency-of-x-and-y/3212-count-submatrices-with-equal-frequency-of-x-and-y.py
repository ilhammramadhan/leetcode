from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        valid_submatrix_count = 0
        
        # Arrays to store the submatrix counts from (0,0) down to the previous row (i-1)
        prev_x_totals = [0] * cols
        prev_y_totals = [0] * cols
        
        for i in range(rows):
            # Running totals for the current row 'i' from column 0 up to 'j'
            current_row_x = 0
            current_row_y = 0
            
            for j in range(cols):
                # Update current row running counts
                if grid[i][j] == 'X':
                    current_row_x += 1
                elif grid[i][j] == 'Y':
                    current_row_y += 1
                    
                # Calculate the grand total for the submatrix (0,0) to (i,j)
                total_x = prev_x_totals[j] + current_row_x
                total_y = prev_y_totals[j] + current_row_y
                
                # Check if this submatrix meets the problem's criteria
                if total_x == total_y and total_x > 0:
                    valid_submatrix_count += 1
                    
                # Store the grand total for the next row to use
                prev_x_totals[j] = total_x
                prev_y_totals[j] = total_y
                
        return valid_submatrix_count