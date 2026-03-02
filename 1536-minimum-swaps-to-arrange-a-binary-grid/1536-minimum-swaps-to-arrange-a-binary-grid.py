from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zero_counts = []
        
        # Step 1: Calculate trailing zeros for each row
        for row in grid:
            count = 0
            # Traverse the row in reverse to count trailing zeros
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            zero_counts.append(count)
            
        ans = 0
        
        # Step 2: Iterate through each row position to place the correct row
        for i in range(n):
            target = n - 1 - i  # Required trailing zeros for row i
            found_idx = -1
            
            # Step 3: Find the closest row that satisfies the requirement
            for j in range(i, n):
                if zero_counts[j] >= target:
                    found_idx = j
                    break
                    
            # If no valid row is found, it's impossible to fix the grid
            if found_idx == -1:
                return -1
                
            # Step 4: Calculate swaps and update the list
            ans += found_idx - i
            
            # Pop the found row and insert it at the current target position 'i'
            # This perfectly simulates adjacent swaps shifting intermediate rows down
            valid_row_zeros = zero_counts.pop(found_idx)
            zero_counts.insert(i, valid_row_zeros)
            
        return ans