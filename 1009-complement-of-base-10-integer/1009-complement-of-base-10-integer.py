class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        mask = 0
        temp = n
        while temp > 0:
            # Shift mask left and add a 1
            mask = (mask << 1) | 1
            # Move through n
            temp >>= 1
            
        return n ^ mask