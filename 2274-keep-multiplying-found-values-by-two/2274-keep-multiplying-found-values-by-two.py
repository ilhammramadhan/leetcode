from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Step 1: Convert the list to a set for O(1) average time complexity lookups.
        num_set = set(nums)
        
        # Step 2: Start the loop. The loop continues as long as 'original' 
        # is found in the set.
        while original in num_set:
            # Step 3: If found, multiply 'original' by 2.
            original *= 2
        
        # Step 5: When the loop stops (because 'original' is not found), 
        # return the final value.
        return original

# Example 1 dry run:
# nums = [5, 3, 6, 1, 12], original = 3
# num_set = {1, 3, 5, 6, 12}
# 
# 1. while 3 in num_set (True): original becomes 6
# 2. while 6 in num_set (True): original becomes 12
# 3. while 12 in num_set (True): original becomes 24
# 4. while 24 in num_set (False): Loop terminates.
# 5. Return 24.