from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Step 1: Initialize a (n+1) x (n+1) matrix with zeros.
        # We use n+1 to safely handle indices like r2+1 or c2+1 without checking bounds.
        mat = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Step 2: Process each query using the Difference Array technique
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1          # Top-left: Start increment
            mat[r1][c2 + 1] -= 1      # Top-right (+1): Stop increment horizontally
            mat[r2 + 1][c1] -= 1      # Bottom-left (+1): Stop increment vertically
            mat[r2 + 1][c2 + 1] += 1  # Bottom-right (+1): Correction factor
            
        # Step 3: Compute Prefix Sums to propagate the values
        
        # 3a. Sweep Horizontally (Row by Row)
        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]
                
        # 3b. Sweep Vertically (Column by Column)
        for r in range(1, n):
            for c in range(n):
                mat[r][c] += mat[r - 1][c]
                
        # Step 4: Return the matrix, discarding the extra padding row and column
        # We only need rows 0 to n-1 and cols 0 to n-1
        result = []
        for r in range(n):
            result.append(mat[r][:n])
            
        return result