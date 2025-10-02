class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        # Step 1: Drink all initial bottles.
        # total_drunk starts with the initial number of bottles.
        total_drunk = numBottles
        
        # These bottles are now empty.
        empty_bottles = numBottles

        # Step 2: Start a loop to handle exchanges.
        # Keep looping as long as we have enough empty bottles for the current exchange cost.
        while empty_bottles >= numExchange:
            
            # Step 3a: Trade 'numExchange' empty bottles.
            empty_bottles -= numExchange
            
            # Step 3b: Get a new full bottle and immediately drink it.
            total_drunk += 1
            
            # Step 3c: The newly drunk bottle becomes an empty one.
            empty_bottles += 1
            
            # Step 3d: The cost for the next exchange increases.
            numExchange += 1
            
        # Step 4: When the loop ends, return the total count.
        return total_drunk