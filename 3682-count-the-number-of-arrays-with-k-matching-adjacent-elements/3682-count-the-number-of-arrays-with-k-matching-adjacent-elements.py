class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Calculates the number of good arrays of size n with elements in [1, m]
        and exactly k adjacent equal elements.
        """
        MOD = 10**9 + 7

        # Edge Case: It's impossible to have k equal pairs if k >= n,
        # as there are only n-1 adjacent pairs in total.
        if k >= n:
            return 0

        # Helper function for modular exponentiation: (a^b) % MOD
        # It's more efficient than the naive loop.
        def power(a, b):
            return pow(a, b, MOD)

        # Helper function for modular inverse: (1/n) % MOD
        # Using Fermat's Little Theorem: a^(p-2) is the modular inverse of a mod p.
        def inverse(n):
            return power(n, MOD - 2)

        # Helper function to calculate combinations C(n, k) % MOD
        # C(n, k) = n! / (k! * (n-k)!)
        # With modulo: (n! * modInverse(k!) * modInverse((n-k)!)) % MOD
        def combinations(n_val, k_val):
            if k_val < 0 or k_val > n_val:
                return 0
            if k_val == 0 or k_val == n_val:
                return 1
            # Optimization: C(n, k) is the same as C(n, n-k)
            if k_val > n_val // 2:
                k_val = n_val - k_val
            
            # Calculate numerator: n * (n-1) * ... * (n-k+1)
            numerator = 1
            for i in range(k_val):
                numerator = (numerator * (n_val - i)) % MOD
            
            # Calculate denominator: k!
            denominator = 1
            for i in range(1, k_val + 1):
                denominator = (denominator * i) % MOD
            
            # Final result is (numerator / denominator) % MOD
            return (numerator * inverse(denominator)) % MOD

        # --- Main Calculation ---

        # 1. Number of ways to choose k positions for equal pairs from n-1 total positions.
        # This is C(n-1, k).
        num_ways_to_choose_positions = combinations(n - 1, k)

        # 2. Number of ways to fill the values.
        # The first element has 'm' choices.
        # The remaining (n-1-k) positions (which must be different from their predecessor)
        # each have 'm-1' choices.
        num_ways_to_fill_values = (m * power(m - 1, n - 1 - k)) % MOD

        # 3. The final answer is the product of these two parts.
        total_good_arrays = (num_ways_to_choose_positions * num_ways_to_fill_values) % MOD
        
        return total_good_arrays
        