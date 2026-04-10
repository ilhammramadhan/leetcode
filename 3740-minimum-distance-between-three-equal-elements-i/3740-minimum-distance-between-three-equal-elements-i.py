from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Step 1: Map each value to a list of its indices
        pos_map = defaultdict(list)
        for idx, val in enumerate(nums):
            pos_map[val].append(idx)
        
        min_dist = float('inf')
        found = False
        
        # Step 2: Iterate through the groups of indices
        for val in pos_map:
            indices = pos_map[val]
            
            # We need at least 3 indices to form a good tuple
            if len(indices) >= 3:
                found = True
                # Step 3: Check consecutive triplets (i, j, k)
                # The distance is 2 * (indices[k] - indices[i])
                for x in range(len(indices) - 2):
                    # We look at triplet starting at index x and ending at x+2
                    i = indices[x]
                    k = indices[x + 2]
                    
                    current_dist = 2 * (k - i)
                    if current_dist < min_dist:
                        min_dist = current_dist
        
        # Step 4: Return result or -1 if no triplet was found
        return min_dist if found else -1