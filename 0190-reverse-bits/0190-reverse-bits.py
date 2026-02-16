class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            # Extract the rightmost bit of n
            bit = n & 1 
            
            # Shift result left by 1 and append the extracted bit
            result = (result << 1) | bit 
            
            # Shift n right by 1 to process the next bit
            n >>= 1 
            
        return result