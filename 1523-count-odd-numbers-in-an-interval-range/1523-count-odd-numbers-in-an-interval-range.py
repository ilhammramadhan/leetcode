class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Step 1: Calculate half the distance
        # We use // for integer division to drop the decimal
        count = (high - low) // 2
        
        # Step 2: Check the boundaries
        # If low is odd (low % 2 == 1) OR high is odd (high % 2 == 1)
        # We need to include one extra number
        if low % 2 == 1 or high % 2 == 1:
            count += 1
            
        return count