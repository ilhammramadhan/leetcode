from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        Calculates the length of the longest valid subsequence using dynamic programming.
        
        The core idea is that any valid subsequence has elements whose remainders
        modulo k alternate between two values (r1, r2, r1, r2, ...).
        
        We use a DP table, dp[k][k], where dp[prev_rem][curr_rem] stores the 
        length of the longest valid subsequence ending with curr_rem, preceded by prev_rem.
        
        As we iterate through each number in nums, we update the DP table. For a number
        with remainder `c`, it can extend any sequence that ended with a number with
        remainder `p` (where the sequence pattern was `..., c, p`). The new sequence
        pattern `..., p, c` will have a length of 1 + dp[c][p].
        """
        
        # dp[i][j] = length of the longest valid subsequence ending with
        #            a number with remainder j, whose previous element had remainder i.
        dp = [[0] * k for _ in range(k)]
        
        max_length = 0

        # Iterate through each number in the input array.
        for num in nums:
            # Get the remainder of the current number.
            curr_rem = num % k
            
            # For every possible remainder of a preceding element...
            for prev_rem in range(k):
                # The new subsequence ending in (... prev_rem, curr_rem)
                # is formed by extending a subsequence ending in (... curr_rem, prev_rem).
                # The length of that previous subsequence is dp[curr_rem][prev_rem].
                # We add 1 for the current number.
                
                # If dp[curr_rem][prev_rem] was 0, it means we are forming a new
                # subsequence of length 2 (represented as 1 + 0 = 1 in the dp table).
                # To get the actual length, we will simply find the max value in the
                # table and add 1 at the end. An alternative is to initialize
                # all lengths to 1, but this approach is cleaner.
                
                dp[prev_rem][curr_rem] = 1 + dp[curr_rem][prev_rem]
                
                # Update the overall maximum length found so far.
                max_length = max(max_length, dp[prev_rem][curr_rem])

        return max_length