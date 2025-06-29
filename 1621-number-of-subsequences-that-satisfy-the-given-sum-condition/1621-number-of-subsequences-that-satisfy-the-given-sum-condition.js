/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {
     nums.sort((a, b) => a - b); // Sort the array in ascending order
    const n = nums.length;
    let left = 0, right = n - 1;
    let count = 0;
    
    // Precompute powers of 2 for efficiency
    const mod = 1e9 + 7;
    const powerOfTwo = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        powerOfTwo[i] = (powerOfTwo[i - 1] * 2) % mod;
    }
    
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            count = (count + powerOfTwo[right - left]) % mod; // Count valid subsequences
            left++;
        } else {
            right--; // Move the right pointer to find a smaller sum
        }
    }
    
    return count;
};