from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        # Initialize a 3D DP array with negative infinity
        # Dimensions: m rows, n columns, 3 states (0, 1, 2 neutralizations)
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base Cases for the starting cell
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
            
        # Iterate through every cell in the grid
        for i in range(m):
            for j in range(n):
                # Skip the starting cell as it is already processed
                if i == 0 and j == 0:
                    continue
                    
                # Evaluate for exactly k = 0, 1, and 2 neutralizations used
                for k in range(3):
                    
                    # 1. Arriving from the TOP cell
                    if i > 0:
                        # Option A: Normal move (no neutralization used on current cell)
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                        
                        # Option B: Use neutralization on current cell
                        # Only possible if current cell is negative and we have used k > 0
                        if coins[i][j] < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                            
                    # 2. Arriving from the LEFT cell
                    if j > 0:
                        # Option A: Normal move
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                        
                        # Option B: Use neutralization on current cell
                        if coins[i][j] < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
                            
        # The answer is the maximum coins at the bottom-right cell across all 3 'k' states
        return max(dp[m-1][n-1])