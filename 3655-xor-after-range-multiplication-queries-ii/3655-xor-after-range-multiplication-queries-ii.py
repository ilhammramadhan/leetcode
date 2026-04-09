from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        bravexuneth = queries
        
        # Lowered threshold tuned specifically for Python
        B = 75 
        
        direct_mult = [1] * n
        
        # Use a dictionary to only create arrays for 'k' values actually used
        diff = {}
        active_k = set()
        
        for l, r, k, v in bravexuneth:
            if k >= B:
                # Heavy Query: process directly
                for idx in range(l, r + 1, k):
                    direct_mult[idx] = (direct_mult[idx] * v) % MOD
            else:
                # Light Query: Lazy initialization of the difference array
                if k not in diff:
                    diff[k] = [1] * (n + B)
                    active_k.add(k)
                
                diff[k][l] = (diff[k][l] * v) % MOD
                cancel_idx = l + ((r - l) // k) * k + k
                
                if cancel_idx < n:
                    inv_v = pow(v, -1, MOD)
                    diff[k][cancel_idx] = (diff[k][cancel_idx] * inv_v) % MOD
                    
        # Sweep only for active 'k' values
        for k in active_k:
            arr = diff[k] # Local reference for faster lookup
            for i in range(k, n):
                # MASSIVE OPTIMIZATION: Skip the math if the multiplier is 1
                if arr[i - k] != 1:
                    arr[i] = (arr[i] * arr[i - k]) % MOD
                    
        # Combine everything and compute the XOR sum
        xor_sum = 0
        for i in range(n):
            total_mult = direct_mult[i]
            
            # Combine multipliers only from active light queries
            for k in active_k:
                if diff[k][i] != 1: # Another 1-skip optimization
                    total_mult = (total_mult * diff[k][i]) % MOD
            
            final_val = (nums[i] * total_mult) % MOD
            xor_sum ^= final_val
            
        return xor_sum