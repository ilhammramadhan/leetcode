class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        # Step 1: Pre-processing
        counts = []
        if not word:
            return 0
        
        # Group consecutive characters and get their counts
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            counts.append(j - i)
            i = j
        
        m = len(counts)
        
        # Calculate total possible combinations
        total_ways = 1
        for c in counts:
            total_ways = (total_ways * c) % MOD
            
        # If the smallest possible string (length m) is already >= k, all combinations are valid
        if m >= k:
            return total_ways

        # Group counts by their frequency
        freq_map = collections.Counter(counts)

        # Precompute modular inverses up to k-1
        inv = [1] * k
        if k > 1:
            inv[1] = 1
            for i in range(2, k):
                inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

        # Step 3a: Calculate ln(P_adj(x))
        # B(x) = ln(P_adj(x)) = sum over (c,f) [f * ln(1+...+x^(c-1))]
        ln_P_adj_coeffs = [0] * k
        for c, f in freq_map.items():
            for j in range(1, k):
                # Add f * (1/j) from the -ln(1-x) term
                term = (f * inv[j]) % MOD
                ln_P_adj_coeffs[j] = (ln_P_adj_coeffs[j] + term) % MOD
                # Subtract f * (1/(j/c)) from the ln(1-x^c) term
                if j % c == 0:
                    sub_term = (f * inv[j // c]) % MOD
                    ln_P_adj_coeffs[j] = (ln_P_adj_coeffs[j] - sub_term + MOD) % MOD

        # Step 3b: Calculate exp(ln_P_adj(x))
        # P_adj(x) = exp(ln_P_adj_coeffs)
        P_adj_coeffs = [0] * k
        P_adj_coeffs[0] = 1
        # Using formula: p_j = (1/j) * sum_{i=1 to j} (i * b_i * p_{j-i})
        for j in range(1, k):
            val = 0
            for i in range(1, j + 1):
                term = (P_adj_coeffs[j - i] * ln_P_adj_coeffs[i]) % MOD
                term = (term * i) % MOD
                val = (val + term) % MOD
            P_adj_coeffs[j] = (val * inv[j]) % MOD

        # Step 4: Sum results for lengths < k
        # Sum coefficients of P_adj(x) for powers 0 to k-1-m
        ways_less_than_k = 0
        for i in range(k - m):
            ways_less_than_k = (ways_less_than_k + P_adj_coeffs[i]) % MOD
        
        # Final answer
        return (total_ways - ways_less_than_k + MOD) % MOD