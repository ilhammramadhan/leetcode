class Solution {
public:
    string largestGoodInteger(string num) {
        // Step 1: Initialize a string to store the maximum good integer found.
        // It starts empty, which is also the value we return if none are found.
        string max_good_integer = "";

        // Step 2: Iterate through the string with a 3-character window.
        // We stop at num.length() - 3 to avoid going out of bounds.
        for (int i = 0; i <= num.length() - 3; ++i) {
            
            // Step 3: Check if all three characters in the window are the same.
            if (num[i] == num[i+1] && num[i+1] == num[i+2]) {
                
                // If they are, we've found a "good integer".
                // Create a substring for this good integer.
                string current_good = num.substr(i, 3);
                
                // Step 4: Compare it with the max we've found so far and update if it's larger.
                // For digit-strings of the same length, lexicographical > is the same as numerical >.
                if (current_good > max_good_integer) {
                    max_good_integer = current_good;
                }
            }
        }
        
        // Step 5: Return the result. It's either the largest good integer or "" if none were found.
        return max_good_integer;
    }
};