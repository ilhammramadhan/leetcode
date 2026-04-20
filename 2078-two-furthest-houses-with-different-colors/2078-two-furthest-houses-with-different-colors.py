from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Step 2: Distance from the first house (index 0)
        # Scan from right to left
        dist_from_start = 0
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                dist_from_start = i
                break # Found the furthest, no need to keep checking
                
        # Step 3: Distance from the last house (index n-1)
        # Scan from left to right
        dist_from_end = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                dist_from_end = (n - 1) - i
                break # Found the furthest, no need to keep checking
                
        # Step 4: Return the maximum of the two distances
        return max(dist_from_start, dist_from_end)