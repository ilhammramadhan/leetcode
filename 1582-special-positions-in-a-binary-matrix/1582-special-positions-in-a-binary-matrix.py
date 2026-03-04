from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        m = len(mat)    # Number of rows
        n = len(mat[0]) # Number of columns
        
        # Step 1: Calculate the sum of 1s in each row
        # row_sums[i] will be the sum of row i
        row_sums = [sum(row) for row in mat]
        
        # Step 2: Calculate the sum of 1s in each column
        # col_sums[j] will be the sum of column j
        col_sums = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        special_count = 0
        
        # Step 3: Find the special positions
        for i in range(m):
            for j in range(n):
                # Check if the current element is 1 AND its row sum is 1 AND its col sum is 1
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
                    
        return special_count