class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Calculates the length of the longest valid subsequence.

        A valid subsequence has a consistent parity for the sum of its adjacent elements.
        This leads to three possible patterns for the longest valid subsequence:
        1. All elements are even.
        2. All elements are odd.
        3. Elements have alternating parities (even, odd, even, odd...).
        
        The algorithm calculates the maximum possible length for each of these three patterns
        and returns the largest of the three.
        """
        
        # --- Case 1 & 2: Subsequences with same-parity elements ---
        # The longest all-even subsequence is the count of all even numbers.
        # The longest all-odd subsequence is the count of all odd numbers.
        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        # --- Case 3: Subsequence with alternating-parity elements ---
        # We find the longest alternating sequence using a greedy approach.
        alternating_len = 0
        # -1 indicates we haven't started the sequence yet.
        # 0 will represent even, 1 will represent odd.
        last_parity = -1 
        
        for num in nums:
            current_parity = num % 2
            # If the current number's parity is different from the last one chosen,
            # we can add it to our alternating subsequence.
            if current_parity != last_parity:
                alternating_len += 1
                last_parity = current_parity

        # The result is the maximum length found among the three possible patterns.
        return max(even_count, odd_count, alternating_len)