from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        
        # This is a cache (memoization) to store results of the helper function
        # to avoid re-computing for the same 'n'.
        memo = {}

        def count_total_transformations(n: int) -> int:
            """
            Correctly calculates the sum of transformations for all numbers in [1, n]
            by iterating through power-of-4 levels.
            ops(i) = k for i in the range [4^(k-1), 4^k - 1].
            """
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            
            total_transforms = 0
            k = 1
            # start_range represents 4^(k-1)
            start_range = 1
            
            while start_range <= n:
                # end_range represents 4^k - 1
                end_range = start_range * 4 - 1
                
                # Count how many numbers in [1, n] fall into the current range
                # where each number requires exactly k operations.
                count = min(n, end_range) - start_range + 1
                
                total_transforms += k * count
                
                # Move to the next power of 4 for the next k
                k += 1
                start_range *= 4
            
            memo[n] = total_transforms
            return total_transforms

        total_ops_sum = 0
        
        for l, r in queries:
            transformations_for_r = count_total_transformations(r)
            transformations_for_l_minus_1 = count_total_transformations(l - 1)
            
            net_transformations = transformations_for_r - transformations_for_l_minus_1
            
            # THE FIX: Use ceiling division instead of integer division.
            # If net_transformations is odd, one extra operation is needed for the last step.
            ops_for_query = (net_transformations + 1) // 2
            
            total_ops_sum += ops_for_query
            
        return total_ops_sum