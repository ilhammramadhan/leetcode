/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
     // Step 1: Initialize your variables
    let left = 0; // The left pointer of the sliding window
    let right = 0; // The right pointer of the sliding window
    
    let maxScore = 0; // To store the maximum sum found so far
    let currentSum = 0; // The sum of the current unique subarray (our window)
    
    const uniqueElements = new Set(); // To keep track of elements currently in our window

    // Step 2: Iterate through the array with the right pointer
    while (right < nums.length) {
        
        // Step 3: Check for duplicates and shrink the window if necessary
        // If the element at the 'right' pointer is already in our set...
        if (uniqueElements.has(nums[right])) {
            // ...we must shrink the window from the left until the duplicate is removed.
            
            // Subtract the leftmost element's value from the current sum
            currentSum -= nums[left];
            // Remove the leftmost element from our set of unique elements
            uniqueElements.delete(nums[left]);
            // Move the left pointer one step to the right
            left++;
            
        } else {
            // Step 4: If no duplicate, expand the window
            
            // Add the new element's value to the current sum
            currentSum += nums[right];
            // Add the new element to our set
            uniqueElements.add(nums[right]);
            
            // Step 5: Update the maximum score
            // We've got a new valid subarray, so see if its sum is the new max
            maxScore = Math.max(maxScore, currentSum);
            
            // Move the right pointer to consider the next element
            right++;
        }
    }
    
    // Step 6: Return the final result
    return maxScore;
};