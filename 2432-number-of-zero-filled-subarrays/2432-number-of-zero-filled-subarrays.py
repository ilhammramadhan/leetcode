from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # total_count will store the final answer.
        total_count = 0
        
        # zeros_in_a_row counts the length of the current consecutive block of zeros.
        zeros_in_a_row = 0
        
        # Iterate through each number in the input array.
        for num in nums:
            if num == 0:
                # If we find a zero, we increment the current streak count.
                zeros_in_a_row += 1
            else:
                # If we find a non-zero, the streak is broken.
                # Calculate the number of subarrays from the previous streak of zeros.
                # The formula for the sum of 1 to k is k * (k + 1) / 2.
                # We use integer division // in Python.
                total_count += (zeros_in_a_row * (zeros_in_a_row + 1)) // 2
                
                # Reset the streak counter.
                zeros_in_a_row = 0
        
        # === Final Check ===
        # After the loop, there might be a trailing sequence of zeros that hasn't been counted yet.
        # For example, in [1, 0, 0], the loop ends before the count for [0,0] is added.
        # So we do the calculation one last time.
        total_count += (zeros_in_a_row * (zeros_in_a_row + 1)) // 2
        
        return total_count