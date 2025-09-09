class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Modulo constant
        MOD = 10**9 + 7

        # dp[i] will store the number of *new* people who learn the secret on day i.
        # We use a size of n+1 for 1-based indexing (day 1 to day n).
        dp = [0] * (n + 1)

        # Base case: On day 1, one person learns the secret.
        dp[1] = 1

        # This variable tracks the number of people who are currently able to share the secret.
        sharing_count = 0

        # Iterate from day 2 to day n to fill the dp array.
        for i in range(2, n + 1):
            
            # 1. ADD new people who can start sharing today.
            # People who learned the secret on day `i - delay` can start sharing today.
            if i - delay > 0:
                sharing_count = (sharing_count + dp[i - delay]) % MOD
            
            # 2. REMOVE people who forget the secret today.
            # People who learned on day `i - forget` will forget today and stop sharing.
            if i - forget > 0:
                # Use (a - b + MOD) % MOD for safe subtraction.
                sharing_count = (sharing_count - dp[i - forget] + MOD) % MOD

            # 3. The number of new people today is the number of people currently sharing.
            dp[i] = sharing_count
        
        # The final answer is the sum of all people who learned the secret
        # and have not forgotten it by day `n`.
        # A person who learned on day `j` forgets on day `j + forget`.
        # They know the secret on day `n` if `n < j + forget`, or `j > n - forget`.
        # So, we sum the new people from the last `forget` days.
        total_aware = 0
        for i in range(n - forget + 1, n + 1):
            total_aware = (total_aware + dp[i]) % MOD
            
        return total_aware