class Solution {
public:
    /**
     * @brief Checks if an integer is a power of four.
     * @param n The integer to check.
     * @return True if n is a power of four, otherwise false.
     */
    bool isPowerOfFour(int n) {
        // A number 'n' is a power of four if it meets three conditions:
        // 1. n > 0: It must be positive.
        // 2. (n & (n - 1)) == 0: It must be a power of two. This is a common bitmask trick.
        //    If a number is a power of two, it has only one bit set to '1' in its binary form (e.g., 16 is 10000).
        //    Subtracting 1 flips this bit and all the following bits (e.g., 15 is 01111).
        //    ANDing them together will result in 0.
        // 3. (n - 1) % 3 == 0: The set bit must be in an even position.
        //    Powers of two: 1, 2, 4, 8, 16, 32, ...
        //    Powers of four: 1,    4,    16,    ...
        //    This condition filters out powers of two like 2, 8, 32, etc.
        //    4^x - 1 = (2^x - 1)(2^x + 1), which is always divisible by 3.
        
        return (n > 0) && ((n & (n - 1)) == 0) && ((n - 1) % 3 == 0);
    }
};