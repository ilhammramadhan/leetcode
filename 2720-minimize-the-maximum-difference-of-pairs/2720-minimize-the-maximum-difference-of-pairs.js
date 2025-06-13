/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function(nums, p) {
    if (p === 0) return 0; // If no pairs can be formed, the max distance is 0
    nums.sort((a, b) => a - b); // Sort the array to easily find pairs
    
    const n = nums.length;
    let low = 0 ;
    let high = nums [n-1] - nums[0]; // The maximum possible distance is the difference between the largest and smallest elements 
    let result = high;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        let pairs = 0;
        let i = 0;

        while (i < n - 1) {
            if (nums[i + 1] - nums[i] <= mid) {
                pairs++; // Form a pair
                i += 2; // Move to the next potential pair
            } else {
                i++; // Move to the next element
            }
        }

        if (pairs >= p) {
            result = mid; // Found a valid distance, try for a smaller one
            high = mid - 1;
        } else {
            low = mid + 1; // Increase the distance
        }
    }
    return result; // Return the minimum maximum distance found
};