class Solution {
public:
    // A helper function for modular exponentiation (calculates (base^exp) % MOD).
    long long power(long long base, long long exp) {
        long long res = 1;
        long long MOD = 1e9 + 7;
        base %= MOD;
        while (exp > 0) {
            // If exponent is odd, multiply base with result
            if (exp % 2 == 1) {
                res = (res * base) % MOD;
            }
            // Exponent must be even now, so we can square the base and halve the exponent
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        long long MOD = 1e9 + 7;
        
        // Step 1 & 3: Find all exponents from the binary representation of n.
        // These are the bit positions 'i' where the bit is 1.
        vector<long long> exponents;
        for (int i = 0; i < 31; ++i) {
            if ((n >> i) & 1) {
                exponents.push_back(i);
            }
        }
        
        // Step 4: Create a prefix sum array for the exponents to answer range sum queries quickly.
        vector<long long> prefix_exp(exponents.size() + 1, 0);
        for (int i = 0; i < exponents.size(); ++i) {
            prefix_exp[i + 1] = prefix_exp[i] + exponents[i];
        }
        
        vector<int> answers;
        // Process each query
        for (const auto& q : queries) {
            int left = q[0];
            int right = q[1];
            
            // Find the sum of exponents in the range [left, right] using the prefix sum array.
            long long total_exponent = prefix_exp[right + 1] - prefix_exp[left];
            
            // Step 5: Calculate 2^total_exponent mod MOD using the power function.
            int result = power(2, total_exponent);
            
            answers.push_back(result);
        }
        
        return answers;
    }
};