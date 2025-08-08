class Solution {
public:
    // This is the main function called by the user.
    double soupServings(int n) {
        // Optimization 2: For large n, the probability approaches 1.
        // A cutoff of 4800 is sufficient to pass within the required precision.
        if (n >= 4800) {
            return 1.0;
        }

        // Optimization 1: Scale n into units of 25mL.
        // m = ceil(n / 25.0). In integer math, this is (n + 24) / 25.
        int m = (n + 24) / 25;

        // Memoization table to store results of solve(a, b).
        // Initialize with -1.0 to indicate that a state has not been computed yet.
        memo.resize(m + 1, vector<double>(m + 1, -1.0));

        // Start the recursive calculation from the initial state (m, m).
        return solve(m, m);
    }

private:
    // The memoization table.
    vector<vector<double>> memo;

    // The recursive solver function. a and b are in units of 25mL.
    double solve(int a, int b) {
        // --- Base Cases ---
        // Case 1: Both A and B are empty. Probability is 0.5.
        if (a <= 0 && b <= 0) {
            return 0.5;
        }
        // Case 2: A is empty, but B is not. Probability is 1.
        if (a <= 0) {
            return 1.0;
        }
        // Case 3: B is empty, but A is not. Probability is 0.
        if (b <= 0) {
            return 0.0;
        }

        // --- Memoization Check ---
        // If we have already computed this state, return the stored value.
        if (memo[a][b] > -1.0) {
            return memo[a][b];
        }

        // --- Recursive Step ---
        // Calculate the probability using the recursive formula.
        // The amounts 100, 75, 50, 25 become 4, 3, 2, 1 in our scaled units.
        double probability = 0.25 * (solve(a - 4, b) +
                                      solve(a - 3, b - 1) +
                                      solve(a - 2, b - 2) +
                                      solve(a - 1, b - 3));

        // Store the result in the memo table and return it.
        return memo[a][b] = probability;
    }
};