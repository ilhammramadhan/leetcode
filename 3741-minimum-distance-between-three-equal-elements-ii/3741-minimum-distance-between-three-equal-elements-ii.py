from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Step 1: Map each value to a list of its indices
        index_map = defaultdict(list)
        for i, val in enumerate(nums):
            index_map[val].append(i)
        
        min_dist = float('inf')
        found = False
        
        # Step 2: Iterate through the index lists
        for indices in index_map.values():
            # We need at least 3 occurrences to form a good tuple
            if len(indices) < 3:
                continue
            
            found = True
            # Step 3: Check consecutive triplets
            # The distance for indices (i, j, k) where i < j < k is 2 * (k - i)
            for m in range(len(indices) - 2):
                current_dist = 2 * (indices[m+2] - indices[m])
                if current_dist < min_dist:
                    min_dist = current_dist
        
        # Step 4: Return result or -1 if no triplet was found
        return min_dist if found else -1