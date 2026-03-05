class Solution:
    def minOperations(self, s: str) -> int:
        count_0 = 0
        n = len(s)
        
        for i in range(n):
            # Check what the character *should* be if the string was "010101..."
            # At even indices (0, 2, 4), i % 2 is 0.
            # At odd indices (1, 3, 5), i % 2 is 1.
            expected_char = str(i % 2)
            
            # If the current character doesn't match the expected one, we need a flip
            if s[i] != expected_char:
                count_0 += 1
                
        # The operations for the "101010..." pattern is simply n - count_0
        count_1 = n - count_0
        
        # Return the minimum of the two possible paths
        return min(count_0, count_1)