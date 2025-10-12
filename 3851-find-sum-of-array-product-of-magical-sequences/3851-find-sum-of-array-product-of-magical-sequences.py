from collections import defaultdict

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations (Pascal's Triangle)
        C = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        
        # dp[j] is a dictionary mapping: carry -> [sum_for_0_bits, sum_for_1_bit, ...]
        # dp[j][carry][p]
        dp = [defaultdict(lambda: [0] * (k + 1)) for _ in range(m + 1)]
        
        # Base Case: 0 elements used, 0 carry, 0 set bits, sum is 1.
        dp[0][0][0] = 1

        # Iterate through each number in nums
        for i in range(n):
            num = nums[i]
            # Create a new dp table for this iteration
            new_dp = [defaultdict(lambda: [0] * (k + 1)) for _ in range(m + 1)]
            
            # Precompute powers of the current number
            pows = [1] * (m + 1)
            for p in range(1, m + 1):
                pows[p] = (pows[p-1] * num) % MOD

            # j is the total elements used *after* considering nums[i]
            for j in range(m + 1):
                # c_i is the count of nums[i] we choose to use
                for c_i in range(j + 1):
                    j_prev = j - c_i
                    
                    # This term combines the new c_i elements with the previous j_prev elements
                    term_for_c_i = (C[j][c_i] * pows[c_i]) % MOD
                    
                    # Iterate through all previous carry states
                    for carry_prev, sums_prev in dp[j_prev].items():
                        current_sum_at_pos_i = c_i + carry_prev
                        carry_new = current_sum_at_pos_i // 2
                        bit = current_sum_at_pos_i % 2

                        # Iterate through previous set bit counts
                        for p_prev in range(k + 1 - bit):
                            if sums_prev[p_prev] > 0:
                                p_new = p_prev + bit
                                contribution = (sums_prev[p_prev] * term_for_c_i) % MOD
                                new_dp[j][carry_new][p_new] = (new_dp[j][carry_new][p_new] + contribution) % MOD
            
            dp = new_dp
        
        # Final Calculation
        ans = 0
        final_sums_map = dp[m] # We must have used exactly m elements

        for carry, sums in final_sums_map.items():
            # The remaining bits are in the final carry
            bits_from_carry = bin(carry).count('1')
            
            for p in range(k + 1):
                # If the bits from the first n positions (p) + bits from carry == k
                if p + bits_from_carry == k:
                    ans = (ans + sums[p]) % MOD
                    
        return ans