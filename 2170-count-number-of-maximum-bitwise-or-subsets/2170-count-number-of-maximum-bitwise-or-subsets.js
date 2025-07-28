/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function(nums) {
    // Step 1: Find the maximum possible bitwise OR value.
    // This is achieved by OR-ing all numbers in the array together.
    const maxOr = nums.reduce((acc, val) => acc | val, 0);
    
    // Initialize a counter for the number of subsets that result in maxOr.
    let count = 0;
    
    /**
     * A recursive function to explore all subsets.
     * @param {number} index - The current index in `nums` to consider.
     * @param {number} currentOr - The bitwise OR of the subset built so far.
     */
    const backtrack = (index, currentOr) => {
        // Base Case: If we have considered all elements in the array.
        if (index === nums.length) {
            // Check if the OR of the generated subset equals the maximum possible OR.
            if (currentOr === maxOr) {
                // If it does, we found a valid subset, so increment the count.
                count++;
            }
            return;
        }
        
        // Recursive Step 1: Include the current element `nums[index]`.
        // We OR the current value with `nums[index]` and move to the next element.
        backtrack(index + 1, currentOr | nums[index]);
        
        // Recursive Step 2: Exclude the current element `nums[index]`.
        // We keep the `currentOr` as is and move to the next element.
        backtrack(index + 1, currentOr);
    };
    
    // Start the backtracking process from the first element (index 0)
    // with an initial OR value of 0 (for an empty set).
    backtrack(0, 0);
    
    return count;
};