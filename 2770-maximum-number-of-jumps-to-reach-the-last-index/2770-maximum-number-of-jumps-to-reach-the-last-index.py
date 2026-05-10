from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # dp[i] will store the max jumps to reach index i
        # Initialize with -1 to indicate unreachable states
        dp = [-1] * n 
        
        # Base case: 0 jumps needed to reach the starting index
        dp[0] = 0 
        
        # Iterate through every index we want to land on
        for i in range(1, n):
            # Check all possible starting indices before 'i'
            for j in range(i):
                
                # 1. dp[j] != -1: ensure we can actually reach index j
                # 2. abs(...) <= target: ensure the jump is within target bounds
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    
                    # Update dp[i] with the maximum jumps found so far
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # The last element holds the max jumps to reach index n-1
        # If it was never reached, it will remain -1
        return dp[-1]