import collections
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        ## Step 1: Count the frequency of each remainder
        # We create a list `counts` of size `value` initialized to all zeros.
        # counts[i] will store how many numbers in `nums` have a remainder of `i`.
        counts = [0] * value
        
        for num in nums:
            # The modulo operator '%' in Python handily gives a non-negative 
            # remainder in the range [0, value-1] when `value` is positive.
            # For example, -1 % 5 = 4 and -10 % 5 = 0.
            remainder = num % value
            counts[remainder] += 1
            
        # Example: nums = [1,-10,7,13,6,8], value = 5
        # 1 % 5 = 1
        # -10 % 5 = 0
        # 7 % 5 = 2
        # 13 % 5 = 3
        # 6 % 5 = 1
        # 8 % 5 = 3
        # The final `counts` list will be: [1, 2, 1, 2, 0]
        # (1 zero, 2 ones, 1 two, 2 threes, 0 fours)

        ## Step 2 & 3: Greedily check for 0, 1, 2, ... and find the MEX
        # We will check numbers starting from `mex = 0`.
        # The largest possible MEX is len(nums), because with N numbers, we can't
        # form N+1 distinct non-negative integers (0, 1, ..., N).
        for mex in range(len(nums)):
            # To form the number `mex`, we need a number from the original `nums`
            # which has a remainder of `mex % value`.
            required_remainder = mex % value
            
            # Do we have an available number with this required remainder?
            if counts[required_remainder] > 0:
                # Yes, we do! So we can form `mex`.
                # We "use up" one of the numbers with this remainder.
                counts[required_remainder] -= 1
            else:
                # No, we don't. We have run out of numbers that can be transformed
                # into `mex`. Therefore, `mex` is the smallest non-negative
                # integer we cannot form. This is our answer.
                return mex
        
        # If the loop completes without returning, it means we successfully
        # formed all the numbers from 0 up to len(nums) - 1.
        # In this case, the smallest missing non-negative integer is len(nums).
        return len(nums)