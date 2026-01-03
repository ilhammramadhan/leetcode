class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial counts for n = 1
        aba = 6
        abc = 6
        
        # Iterate from the second row to the nth row
        for _ in range(1, n):
            # Calculate next states based on transition logic
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            
            # Update current counts
            aba, abc = next_aba, next_abc
            
        # The answer is the sum of both types for the nth row
        return (aba + abc) % MOD