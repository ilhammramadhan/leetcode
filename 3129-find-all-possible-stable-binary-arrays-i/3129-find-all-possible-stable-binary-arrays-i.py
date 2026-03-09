class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> stable arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases for purely 0s
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
            
        # Base cases for purely 1s
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1
            
        # Fill the DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # --- Calculate arrays ending in 0 ---
                # Add a 0 to all valid prefixes of size (i-1, j)
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                
                # Subtract the cases where adding this 0 created limit + 1 consecutive 0s
                if i > limit:
                    # In Python, negative modulo is handled safely, but we do + MOD for standard mathematical safety
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                    
                # --- Calculate arrays ending in 1 ---
                # Add a 1 to all valid prefixes of size (i, j-1)
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                
                # Subtract the cases where adding this 1 created limit + 1 consecutive 1s
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                    
        # The result is the sum of valid configurations ending in either 0 or 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD