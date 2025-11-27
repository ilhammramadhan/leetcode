from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize prefix sum and max_sum
        prefix_sum = 0
        max_sum = float('-inf')
        
        # This array stores the minimum prefix sum encountered for each remainder.
        # size is k because remainders can only be 0 to k-1.
        min_prefix = [float('inf')] * k
        
        # Base case: A subarray starting at index 0 has a "previous" prefix sum of 0
        # at a theoretical index 0 (which has remainder 0).
        min_prefix[0] = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            # Use 1-based indexing logic for length calculation usually,
            # but strictly speaking we just need consistency.
            # Here: index i corresponds to the end of a subarray of length (i+1).
            current_index = i + 1
            remainder = current_index % k
            
            # If we have a valid previous prefix sum with the same remainder,
            # we can form a valid subarray.
            if min_prefix[remainder] != float('inf'):
                candidate_sum = prefix_sum - min_prefix[remainder]
                max_sum = max(max_sum, candidate_sum)
            
            # Update the minimum prefix sum for this remainder
            # We want the smallest prefix sum to subtract, to maximize the result.
            min_prefix[remainder] = min(min_prefix[remainder], prefix_sum)
            
        return max_sum