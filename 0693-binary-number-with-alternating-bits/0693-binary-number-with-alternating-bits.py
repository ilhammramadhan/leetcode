class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Loop until we run out of bits to check
        while n > 0:
            # Get the current last bit (e.g., if n is 101, this gets 1)
            current_bit = n & 1
            
            # Look ahead at the next bit (shift right by 1, then get bit)
            # If n is 101, (n >> 1) is 10, so this gets 0
            neighbor_bit = (n >> 1) & 1
            
            # Compare them. If they are the same, it's not alternating.
            if current_bit == neighbor_bit:
                return False
            
            # Shift n to the right to process the next pair
            n = n >> 1
            
        # If we get through the whole number without returning False, it is True
        return True