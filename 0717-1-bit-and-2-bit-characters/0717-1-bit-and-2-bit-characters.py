from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        # Loop while the pointer is strictly BEFORE the last element
        while i < n - 1:
            if bits[i] == 1:
                # If we see a 1, it's a 2-bit char. 
                # Jump 2 steps (skip the next bit).
                i += 2
            else:
                # If we see a 0, it's a 1-bit char.
                # Jump 1 step.
                i += 1
                
        # If i lands exactly on the last index (n - 1), 
        # it means the last bit is the start of a new character.
        return i == n - 1