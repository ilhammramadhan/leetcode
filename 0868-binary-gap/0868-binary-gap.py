class Solution:
    def binaryGap(self, n: int) -> int:
        # 1. Convert n to binary string (e.g., 22 -> '10110')
        binary_str = bin(n)[2:]
        
        max_gap = 0
        last_pos = None
        
        # 2. Iterate through the string with indices
        for i, bit in enumerate(binary_str):
            if bit == '1':
                # If we've seen a 1 before, calculate the distance
                if last_pos is not None:
                    max_gap = max(max_gap, i - last_pos)
                
                # Update last_pos to the current index
                last_pos = i
                
        return max_gap