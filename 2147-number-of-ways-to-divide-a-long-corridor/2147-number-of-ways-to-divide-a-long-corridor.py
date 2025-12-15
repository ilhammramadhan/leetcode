class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Step 1: Collect indices of all seats
        seats = [i for i, char in enumerate(corridor) if char == 'S']
        
        # Step 2: Validity check
        # If no seats or odd number of seats, valid division is impossible
        if not seats or len(seats) % 2 != 0:
            return 0
        
        result = 1
        MOD = 10**9 + 7
        
        # Step 3: Iterate through gaps between pairs
        # We skip the first pair (indices 0 and 1) and start looking at the gap
        # between index 1 (end of first pair) and index 2 (start of second pair)
        for i in range(2, len(seats), 2):
            prev_seat_index = seats[i - 1]
            curr_seat_index = seats[i]
            
            # The number of ways to place a divider between these two pairs
            # is simply the difference in their indices.
            ways = curr_seat_index - prev_seat_index
            
            # Step 4: Multiply into result with modulo
            result = (result * ways) % MOD
            
        return result