from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Process each query one by one
        for li, ri, ki, vi in queries:
            idx = li
            # Step 2: Traverse from li to ri with step ki
            while idx <= ri:
                # Apply the multiplication and modulo
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        
        # Step 3: Compute the bitwise XOR of the final array
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans