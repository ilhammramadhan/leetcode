from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Get the total number of magicians.
        n = len(energy)
        
        # We will iterate backwards through the array.
        # This is the core of the dynamic programming approach.
        # For each index 'i', we calculate the total energy of the path starting at 'i'.
        # To do this, we need the total energy of the path starting at 'i + k',
        # which will have already been calculated because we are moving backwards.
        for i in range(n - 1, -1, -1):
            
            # Check if a jump from magician 'i' is possible (i.e., lands within the array).
            next_index = i + k
            if next_index < n:
                # If the jump is possible, the total energy from starting at 'i'
                # is its own energy plus the already computed total energy from 'i + k'.
                energy[i] += energy[next_index]
        
        # After the loop, the 'energy' array has been modified.
        # Each element energy[i] now holds the sum of the entire path starting from i.
        # The problem asks for the maximum possible energy, so we just find the max
        # value in our updated array.
        return max(energy)