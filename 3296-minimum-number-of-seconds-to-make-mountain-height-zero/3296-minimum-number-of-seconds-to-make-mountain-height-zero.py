import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Step 2: Define the search boundaries
        low = 1
        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        
        # Step 3: Feasibility check function
        def canFinish(target_time: int) -> bool:
            total_reduced = 0
            
            for w in workerTimes:
                # Using the derived quadratic formula to find max x for this worker
                # x = (sqrt(1 + 8 * T / w) - 1) // 2
                x = (math.isqrt(1 + 8 * target_time // w) - 1) // 2
                total_reduced += x
                
                # Early exit if we already reached the required mountain height
                if total_reduced >= mountainHeight:
                    return True
                    
            return total_reduced >= mountainHeight

        # Step 4: Binary Search
        ans = high
        while low <= high:
            mid = (low + high) // 2
            
            if canFinish(mid):
                ans = mid       # Record the valid time
                high = mid - 1  # Try to find a smaller valid time
            else:
                low = mid + 1   # We need more time
                
        return ans