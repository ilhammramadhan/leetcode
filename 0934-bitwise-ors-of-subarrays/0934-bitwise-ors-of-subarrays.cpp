#include <vector>
#include <unordered_set>

class Solution {
public:
    int subarrayBitwiseORs(std::vector<int>& arr) {
        // This set will store all unique bitwise ORs found.
        std::unordered_set<int> result;
        
        // This set stores the bitwise ORs of all subarrays ending at the previous position.
        std::unordered_set<int> current;

        // Iterate through each number in the input array.
        for (int num : arr) {
            // This set will store the bitwise ORs of all subarrays ending at the current number.
            std::unordered_set<int> next;
            
            // The subarray consisting of just the current number is a valid possibility.
            next.insert(num);
            
            // For each result from the previous step, create a new result by ORing with the current number.
            // This extends all previous subarrays with the current number.
            for (int prev_or : current) {
                next.insert(prev_or | num);
            }
            
            // Add all the newly found ORs for subarrays ending at the current position to our global result set.
            result.insert(next.begin(), next.end());
            
            // The 'next' set now becomes the 'current' set for the next iteration.
            // Using std::move is a small optimization to avoid a copy.
            current = std::move(next);
        }
        
        // The size of the result set is the number of distinct bitwise ORs.
        return result.size();
    }
};