/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    // Step 1: Get all unique numbers from the input array.
  const uniqueNums = new Set(nums);

  // Step 2: Calculate the sum of all unique positive numbers.
  let maxSum = 0;
  for (const num of uniqueNums) {
    if (num > 0) {
      maxSum += num;
    }
  }

  // Step 3: Handle the edge case and return the final result.
  if (maxSum === 0) {
    // If no positive unique numbers exist, the max sum is the largest
    // element in the array (which could be 0 or negative).
    return Math.max(...nums);
  } else {
    // Otherwise, the sum of unique positive numbers is the maximum sum.
    return maxSum;
  }
};