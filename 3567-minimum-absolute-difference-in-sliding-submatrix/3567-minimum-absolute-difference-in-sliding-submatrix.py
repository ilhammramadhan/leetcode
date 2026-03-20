from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        # Step 1: Initialize the result matrix with 0s
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        # Step 2: Iterate over every possible top-left corner
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                # Step 3: Extract distinct values into a set
                distinct_vals = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_vals.add(grid[r][c])
                
                # Step 4: Calculate minimum absolute difference
                if len(distinct_vals) < 2:
                    ans[i][j] = 0
                else:
                    sorted_vals = sorted(list(distinct_vals))
                    min_diff = float('inf')
                    
                    # Check adjacent elements in the sorted list
                    for v in range(1, len(sorted_vals)):
                        diff = sorted_vals[v] - sorted_vals[v - 1]
                        if diff < min_diff:
                            min_diff = diff
                            
                    ans[i][j] = min_diff
                    
        # Step 5: Return the populated matrix
        return ans