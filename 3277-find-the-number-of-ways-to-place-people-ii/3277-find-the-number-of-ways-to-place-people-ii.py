class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Calculates the number of valid Alice-Bob pairs using an efficient
        O(n^2) approach with sorting.
        """
        # Step 1: Sort points by x-coordinate ascending, then y-coordinate descending.
        # This is the crucial optimization step.
        points.sort(key=lambda p: (p[0], -p[1]))
        
        n = len(points)
        valid_pairs_count = 0
        
        # Step 2: Iterate through each point as a potential Alice.
        for i in range(n):
            alice_x, alice_y = points[i]
            
            # This will track the highest y-coordinate of a valid Bob found so far FOR THIS ALICE.
            max_bob_y = -float('inf') 
            
            # Step 3: Iterate through subsequent points as potential Bobs.
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                
                # We only need to consider points where Bob is "below" Alice,
                # since the sort already guarantees bob_x >= alice_x.
                if bob_y <= alice_y:
                    # THE TRICK: Check if this Bob is "higher" than any previous valid Bob.
                    # If it is, no previous point can be inside the fence.
                    if bob_y > max_bob_y:
                        valid_pairs_count += 1
                        # Update the max_y for this Alice.
                        max_bob_y = bob_y
                        
        return valid_pairs_count