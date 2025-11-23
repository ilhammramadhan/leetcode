from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Step 1: Calculate the total sum
        total_sum = sum(nums)
        
        # Step 2: Check the remainder of the total sum
        remainder = total_sum % 3
        
        # If divisible by 3, we are done
        if remainder == 0:
            return total_sum
        
        # Step 3: separate numbers by their remainder logic
        # We only need the smallest ones, so we can collect and sort them
        rem_1 = sorted([x for x in nums if x % 3 == 1])
        rem_2 = sorted([x for x in nums if x % 3 == 2])
        
        to_remove = float('inf')
        
        # Step 4: Determine what to remove based on the remainder
        if remainder == 1:
            # Option A: Remove one number with remainder 1
            if len(rem_1) >= 1:
                to_remove = min(to_remove, rem_1[0])
            # Option B: Remove two numbers with remainder 2 (2+2=4 -> rem 1)
            if len(rem_2) >= 2:
                to_remove = min(to_remove, rem_2[0] + rem_2[1])
                
        elif remainder == 2:
            # Option A: Remove one number with remainder 2
            if len(rem_2) >= 1:
                to_remove = min(to_remove, rem_2[0])
            # Option B: Remove two numbers with remainder 1 (1+1=2 -> rem 2)
            if len(rem_1) >= 2:
                to_remove = min(to_remove, rem_1[0] + rem_1[1])
        
        # If we found a valid set of numbers to remove, subtract them.
        # Otherwise (if we couldn't fix the remainder), return 0.
        if to_remove == float('inf'):
            return 0
            
        return total_sum - to_remove