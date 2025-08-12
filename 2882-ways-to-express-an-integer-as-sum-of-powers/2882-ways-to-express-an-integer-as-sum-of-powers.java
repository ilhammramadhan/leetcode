class Solution {
    public int numberOfWays(int n, int x) {
        // Define the modulus for the final result.
        int MOD = 1_000_000_007;
        
        // dp[i] will store the number of ways to get sum 'i'.
        // The array is of type long to prevent intermediate overflow before the modulo,
        // though applying modulo at each step with int also works.
        // Let's stick to the problem's int return type and apply modulo frequently.
        int[] dp = new int[n + 1];
        
        // Base case: There is 1 way to make a sum of 0 (by choosing nothing).
        dp[0] = 1;
        
        // Outer loop: Iterate through each possible base number (1, 2, 3, ...).
        // We only need to consider numbers whose x-th power is not greater than n.
        for (int num = 1; ; num++) {
            // Calculate the x-th power of the current number.
            int power = (int) Math.pow(num, x);
            
            // If the power exceeds n, we can't use this number or any larger ones.
            // So, we can stop.
            if (power > n) {
                break;
            }
            
            // Inner loop: Update the dp table.
            // Iterate backwards from n down to the current power value.
            // This is crucial to ensure each number's power is used at most once.
            for (int j = n; j >= power; j--) {
                // The new number of ways to form sum 'j' is the current number of ways
                // plus the number of ways to form sum 'j - power'.
                dp[j] = (dp[j] + dp[j - power]) % MOD;
            }
        }
        
        // The final answer is the number of ways to form the sum 'n'.
        return dp[n];
    }
}