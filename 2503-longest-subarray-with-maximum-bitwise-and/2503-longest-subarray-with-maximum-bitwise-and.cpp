#include <vector>
#include <algorithm> // Required for std::max

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        // Step 1: Find the maximum element in the array.
        // We initialize max_val to 0, as constraints state nums[i] >= 1.
        int max_val = 0;
        for (int num : nums) {
            if (num > max_val) {
                max_val = num;
            }
        }
        // A more concise C++ way to find the max element is:
        // int max_val = *std::max_element(nums.begin(), nums.end());

        // Step 2: Find the length of the longest contiguous subarray of max_val.
        int max_length = 0;
        int current_length = 0;
        
        for (int num : nums) {
            // If the current number is the maximum value, we extend the current subarray.
            if (num == max_val) {
                current_length++;
            } else {
                // If the sequence of max_val is broken, update the overall max_length
                // with the length of the sequence that just ended.
                max_length = std::max(max_length, current_length);
                // Reset the current counter.
                current_length = 0;
            }
        }
        
        // After the loop, it's possible the longest subarray was at the very end.
        // So, we do one final check to update max_length.
        max_length = std::max(max_length, current_length);
        
        return max_length;
    }
};