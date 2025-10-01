class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # We can definitely drink all the bottles we start with.
        total_drunk = numBottles
        
        # After drinking them, they all become empty.
        empty_bottles = numBottles
        
        # Keep exchanging as long as we have enough empty bottles for a trade.
        while empty_bottles >= numExchange:
            # 1. Calculate how many new full bottles we can get from the exchange.
            # We use integer division // because we can't get a fraction of a bottle.
            new_full_bottles = empty_bottles // numExchange
            
            # 2. These new bottles will be drunk, so add them to our total.
            total_drunk += new_full_bottles
            
            # 3. Update the number of empty bottles we have.
            # This is the sum of two parts:
            #   a) The bottles that were "left over" from the exchange (using modulo %).
            #   b) The new empty bottles we get after drinking the `new_full_bottles`.
            empty_bottles = (empty_bottles % numExchange) + new_full_bottles
            
        return total_drunk