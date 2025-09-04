class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Step 1: Calculate the absolute distance from Person 1 (x) to Person 3 (z).
        dist1 = abs(x - z)
        
        # Step 2: Calculate the absolute distance from Person 2 (y) to Person 3 (z).
        dist2 = abs(y - z)
        
        # Step 3: Compare the two distances to determine the result.
        if dist1 < dist2:
            # Person 1 is closer, so they arrive first.
            return 1
        elif dist2 < dist1:
            # Person 2 is closer, so they arrive first.
            return 2
        else:
            # The distances are equal, so they arrive at the same time.
            return 0