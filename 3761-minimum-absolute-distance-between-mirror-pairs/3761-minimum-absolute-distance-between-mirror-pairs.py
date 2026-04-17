from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Initialize the minimum distance to infinity
        min_dist = float('inf')
        
        # Dictionary to map: reverse(nums[i]) -> index i
        seen_reversed = {}
        
        for j, val in enumerate(nums):
            # If the current number matches a previously stored reversed number
            if val in seen_reversed:
                # Calculate distance and update the minimum distance
                dist = j - seen_reversed[val]
                if dist < min_dist:
                    min_dist = dist
            
            # Reverse the current number to store for future iterations.
            # int(str(val)[::-1]) naturally handles the omission of leading zeros.
            rev_val = int(str(val)[::-1])
            
            # Store/overwrite the index of this reversed value.
            # We always want the most recent index to get the minimum absolute distance.
            seen_reversed[rev_val] = j
            
        # Return the minimum distance if found, otherwise return -1
        return min_dist if min_dist != float('inf') else -1