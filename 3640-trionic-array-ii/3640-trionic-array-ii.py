from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Initialize states to negative infinity
        # These states represent the max sum ending at index (i-1)
        # obeying the specific structural constraints.
        inc = -float('inf')  # Increasing leg (len >= 2)
        dec = -float('inf')  # Inc -> Dec (Dec leg len >= 2)
        tri = -float('inf')  # Inc -> Dec -> Inc (Final Inc leg len >= 2)
        
        ans = -float('inf')
        
        for i in range(1, n):
            curr = nums[i]
            prev = nums[i-1]
            
            # Temporary variables for the new states at index i
            new_inc = -float('inf')
            new_dec = -float('inf')
            new_tri = -float('inf')
            
            # 1. Update Increasing Leg (nums[l...p])
            # Must be strictly increasing.
            if curr > prev:
                # Option A: Extend an existing valid increasing sequence
                # Option B: Start a new increasing sequence of length 2 [prev, curr]
                # We do this because Option A might carry a heavy negative prefix
                new_inc = max(inc + curr, prev + curr)
                
            # 2. Update Decreasing Leg (nums[p...q])
            # Must be strictly decreasing.
            if curr < prev:
                # Option A: Extend existing decreasing sequence
                if dec != -float('inf'):
                    new_dec = max(new_dec, dec + curr)
                
                # Option B: Transition from Increasing -> Decreasing
                # We can only transition if we had a valid increasing leg (len >= 2)
                if inc != -float('inf'):
                    new_dec = max(new_dec, inc + curr)
            
            # 3. Update Trionic Leg (nums[q...r])
            # Must be strictly increasing.
            if curr > prev:
                # Option A: Extend existing trionic sequence
                if tri != -float('inf'):
                    new_tri = max(new_tri, tri + curr)
                
                # Option B: Transition from Decreasing -> Increasing
                # We can only transition if we had a valid decreasing leg
                if dec != -float('inf'):
                    new_tri = max(new_tri, dec + curr)
            
            # Update states for next iteration
            inc = new_inc
            dec = new_dec
            tri = new_tri
            
            # Track the global maximum for the full trionic structure
            if tri != -float('inf'):
                ans = max(ans, tri)
                
        return ans