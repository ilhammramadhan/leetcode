import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        # Loop through all possible values for 'a'
        for a in range(1, n + 1):
            # Loop through all possible values for 'b'
            for b in range(1, n + 1):
                
                # Calculate the hypotenuse squared
                val = a**2 + b**2
                
                # Calculate the square root (c)
                c = int(math.sqrt(val))
                
                # Validation Logic:
                # 1. c * c == val checks if 'val' was a perfect square 
                #    (e.g., if val=5, c=2, c*c=4 != 5. Not a perfect square).
                # 2. c <= n checks if the resulting number is within bounds.
                if c * c == val and c <= n:
                    count += 1
                    
        return count