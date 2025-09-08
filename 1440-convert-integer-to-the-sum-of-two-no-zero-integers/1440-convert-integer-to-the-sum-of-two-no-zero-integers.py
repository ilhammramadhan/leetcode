from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Step 1: Iterate through all possible values for 'a' from 1 up to n-1.
        for a in range(1, n):
            # Calculate the corresponding value for 'b'.
            b = n - a
            
            # Step 2: Check if both 'a' and 'b' are No-Zero integers.
            # We do this by converting them to strings and checking for the '0' character.
            if '0' not in str(a) and '0' not in str(b):
                # Step 3: If both are No-Zero integers, we've found our answer.
                return [a, b]