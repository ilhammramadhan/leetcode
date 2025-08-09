class Solution {
public:
    bool isPowerOfTwo(int n) {
        // A power of two must be positive and have only one bit set to '1' in its binary form.
        // The expression (n & (n - 1)) == 0 checks for that single '1' bit.
        return n > 0 && (n & (n - 1)) == 0;
    }
};