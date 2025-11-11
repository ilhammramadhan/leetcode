class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # 1. Initialize DP table
        # dp[j][k] = max subset size with at most j zeros and k ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. Iterate through each string (item)
        for s in strs:
            # 3. Calculate the "cost" of this item
            zeros = s.count('0')
            ones = s.count('1')
            
            # 4. Update the DP table
            # We MUST iterate backwards to ensure 0/1 property
            # (i.e., we don't use the same string more than once)
            
            # Start from max zero budget, go down to the cost of this string
            for j in range(m, zeros - 1, -1):
                # Start from max one budget, go down to the cost of this string
                for k in range(n, ones - 1, -1):
                    
                    # At this (j, k) budget, we decide:
                    # Is it better to NOT take the string (keep dp[j][k])
                    # OR to TAKE the string (1 + dp[j - zeros][k - ones])?
                    
                    # dp[j][k] (don't take)
                    # 1 + dp[j-zeros][k-ones] (take)
                    dp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones])
                    
        # 5. The final answer is in the cell for the full budget
        return dp[m][n]