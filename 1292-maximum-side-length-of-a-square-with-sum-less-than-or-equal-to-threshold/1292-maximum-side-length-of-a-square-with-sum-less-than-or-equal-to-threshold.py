from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 1. Initialize Prefix Sum Matrix (extra row/col for padding)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + 
                               prefix[i-1][j] + 
                               prefix[i][j-1] - 
                               prefix[i-1][j-1])
        
        ans = 0
        # 2. Iterate through every possible bottom-right corner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Try to see if we can fit a square larger than our current max 'ans'
                # The square would have side length L = ans + 1
                L = ans + 1
                
                # Check if a square of side L can even fit at this position (i, j)
                if i >= L and j >= L:
                    # Calculate sum of square ending at (i, j) with side L
                    current_sum = (prefix[i][j] - 
                                  prefix[i-L][j] - 
                                  prefix[i][j-L] + 
                                  prefix[i-L][j-L])
                    
                    # If valid, update our answer
                    if current_sum <= threshold:
                        ans += 1
                        
        return ans