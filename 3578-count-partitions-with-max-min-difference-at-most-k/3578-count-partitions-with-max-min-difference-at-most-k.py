from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # dp[i] means number of ways to partition the first i elements (nums[0...i-1])
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # Monotonic deques to store indices
        # max_d stores indices where values are decreasing
        # min_d stores indices where values are increasing
        max_d = deque()
        min_d = deque()
        
        left = 0
        current_sum = 0
        
        for i in range(n):
            # 1. Update max_d: maintain decreasing order
            while max_d and nums[max_d[-1]] <= nums[i]:
                max_d.pop()
            max_d.append(i)
            
            # 2. Update min_d: maintain increasing order
            while min_d and nums[min_d[-1]] >= nums[i]:
                min_d.pop()
            min_d.append(i)
            
            # 3. Add the number of ways to reach the index just before this new segment starts
            #    which is dp[i] (since dp is 1-indexed relative to nums)
            current_sum = (current_sum + dp[i]) % MOD
            
            # 4. Shrink the window from the left if the condition is violated
            #    The valid segment is nums[left...i]
            while nums[max_d[0]] - nums[min_d[0]] > k:
                # If left is moving past a start point, that start point is no longer valid
                # for the current ending 'i'. So we subtract its contribution.
                current_sum = (current_sum - dp[left]) % MOD
                left += 1
                
                # Remove indices that are now out of the window [left, i]
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            # 5. The number of ways to partition up to i+1 is the sum of ways 
            #    for all valid split points in the current window.
            dp[i + 1] = current_sum
            
        return dp[n]