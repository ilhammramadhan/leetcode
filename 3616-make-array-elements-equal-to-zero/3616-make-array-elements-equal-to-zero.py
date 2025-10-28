from typing import List

class Solution:
    
    def _simulate(self, nums: List[int], start_curr: int, start_direction: int) -> bool:
        """
        Runs a single simulation for one starting (position, direction) pair.
        Returns True if the simulation results in all zeros, False otherwise.
        
        start_direction: 1 for 'right', -1 for 'left'.
        """
        
        # 1. Create a copy to avoid modifying the original list
        nums_copy = list(nums)
        n = len(nums_copy)
        
        curr = start_curr
        direction = start_direction
        
        # 2. Run the process while inside the array bounds
        while 0 <= curr < n:
            if nums_copy[curr] == 0:
                # Rule: If 0, move in the current direction
                curr += direction
            else: # nums_copy[curr] > 0
                # Rule: If > 0:
                # 1. Decrement
                nums_copy[curr] -= 1
                # 2. Reverse direction
                direction *= -1 
                # 3. Move in the *new* direction
                curr += direction
                
        # 3. After the loop (out of bounds), check if the process was "valid".
        # Since all numbers are non-negative, the sum will be 0 if and only if
        # all elements are 0.
        return sum(nums_copy) == 0

    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0
        
        # 1. Find all possible starting positions (where num == 0)
        start_indices = [i for i, val in enumerate(nums) if val == 0]
        
        # 2. Iterate through each possible starting position
        for start_index in start_indices:
            
            # 3. For each position, test both starting directions
            
            # Test starting by moving RIGHT (direction = 1)
            if self._simulate(nums, start_index, 1):
                valid_count += 1
                
            # Test starting by moving LEFT (direction = -1)
            if self._simulate(nums, start_index, -1):
                valid_count += 1
        
        # 4. Return the total count of valid selections
        return valid_count