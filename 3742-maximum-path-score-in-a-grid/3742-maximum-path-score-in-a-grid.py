from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Optimization: Cap 'k' at the maximum possible cost a path could take
        max_possible_cost = m + n - 2
        k = min(k, max_possible_cost)
        
        # dp[c][w] stores the max score at column 'c' with exactly 'w' cost
        # We initialize with -1 to denote unreachable states
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        # Base case: The starting cell (0, 0)
        # The prompt guarantees grid[0][0] == 0, so cost=0 and score=0
        dp[0][0] = 0
        
        for r in range(m):
            # Temporary DP table for the current row
            curr_dp = [[-1] * (k + 1) for _ in range(n)]
            
            for c in range(n):
                # Calculate cost and score for the current cell
                cell_val = grid[r][c]
                cell_cost = 1 if cell_val > 0 else 0
                cell_score = cell_val
                
                # Base case carry-over for the very first cell
                if r == 0 and c == 0:
                    curr_dp[0][0] = 0
                    continue
                    
                # Evaluate all possible costs 'w' from previous cells
                for w in range(k + 1 - cell_cost):
                    new_w = w + cell_cost
                    
                    # 1. Coming from the Left (c - 1)
                    if c > 0 and curr_dp[c - 1][w] != -1:
                        curr_dp[c][new_w] = max(curr_dp[c][new_w], curr_dp[c - 1][w] + cell_score)
                        
                    # 2. Coming from Top (r - 1)
                    if r > 0 and dp[c][w] != -1:
                        curr_dp[c][new_w] = max(curr_dp[c][new_w], dp[c][w] + cell_score)
                        
            # Move down to the next row, making the current row our new "previous" row
            dp = curr_dp
            
        # The answer is the maximum score found at the bottom-right cell (n - 1) across all valid costs
        max_score = max(dp[n - 1])
        
        return max_score if max_score != -1 else -1