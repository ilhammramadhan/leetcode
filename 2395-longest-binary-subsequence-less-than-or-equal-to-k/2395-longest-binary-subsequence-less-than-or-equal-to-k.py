class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Calculates the length of the longest subsequence of s that forms a binary
        number less than or equal to k.

        The logic is greedy and works in two main parts:
        1. All '0's can always be included in the subsequence because they provide
           length while contributing minimally to the value (or not at all as 
           leading zeros). We count all of them first.
        2. To maximize the number of '1's we can include, we should pick the 
           '1's with the smallest place values. These are the ones at the
           rightmost positions in the string.

        We iterate from right to left, keeping track of the current numerical value
        formed by the '1's and the place value (power of 2) of the current position.
        """
        
        # Part 1: All '0's are "free" and always contribute to the length.
        num_zeros = s.count('0')
        
        # Part 2: Greedily add '1's from right to left (least significant).
        num_ones = 0
        current_value = 0
        power_of_2 = 1  # Represents 2^0, 2^1, 2^2, ...
        
        # Iterate from the right of the string.
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                # Check if we can afford to add this '1'.
                if current_value + power_of_2 <= k:
                    current_value += power_of_2
                    num_ones += 1
            
            # The place value for the next bit to the left is always double.
            # We must update the power even if the character is '0', because
            # each character represents a potential bit position.
            power_of_2 *= 2
            
            # Optimization: If the next power of 2 itself is greater than k,
            # and our current value is already non-zero, it's impossible
            # to add any more '1's. More simply, if power_of_2 exceeds k,
            # (current_value + power_of_2) will surely exceed k.
            if power_of_2 > k:
                break
                
        # The total length is the sum of all '0's and the '1's we could afford.
        return num_zeros + num_ones