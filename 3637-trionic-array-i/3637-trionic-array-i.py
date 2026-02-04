from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # We need at least 4 elements to form a valid trionic array
        # because p > 0 means minimum index 1, q > p means min index 2,
        # q < n-1 means max index n-2.
        # The shortest pattern is indices 0, 1(p), 2(q), 3.
        if n < 4:
            return False

        # Helper function to check if a subarray is strictly increasing
        def is_increasing(start, end):
            for i in range(start, end):
                if nums[i] >= nums[i+1]:
                    return False
            return True

        # Helper function to check if a subarray is strictly decreasing
        def is_decreasing(start, end):
            for i in range(start, end):
                if nums[i] <= nums[i+1]:
                    return False
            return True

        # Iterate through all possible pivot points p and q
        # p ranges from index 1 to n-3
        # q ranges from p+1 to n-2
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                
                # Check 1: First segment (0 to p) must be Increasing
                if not is_increasing(0, p):
                    continue
                    
                # Check 2: Second segment (p to q) must be Decreasing
                if not is_decreasing(p, q):
                    continue
                    
                # Check 3: Third segment (q to n-1) must be Increasing
                if not is_increasing(q, n - 1):
                    continue
                
                # If all pass, we found a valid trionic configuration
                return True
                
        return False