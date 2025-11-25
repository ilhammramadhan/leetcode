class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Step 1: Check for impossible cases (divisible by 2 or 5)
        # If k is even or ends in 5, no number ending in '1' can be divisible by it.
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        # Step 2: Initialize variables
        remainder = 0
        
        # We iterate from length 1 up to k.
        # It is mathematically proven that if a solution exists, 
        # the length will be <= k.
        for length_n in range(1, k + 1):
            # Step 3: Update the remainder logic
            # Instead of building the huge number '11...1', we just track the remainder.
            # Formula: next_remainder = (prev_remainder * 10 + 1) % k
            remainder = (remainder * 10 + 1) % k
            
            # Step 4: Check if we found the solution
            if remainder == 0:
                return length_n
        
        # If we finish the loop without returning, no solution exists
        return -1