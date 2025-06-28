/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function(nums, k) {
     // Create an array of objects with value and index
    const indexedNums = nums.map((num, index) => ({ value: num, index }));
    
    // Sort the array based on the value in descending order
    indexedNums.sort((a, b) => b.value - a.value);
    
    // // Take the first k elements from the sorted array
    const topK = indexedNums.slice(0, k);
    
    // // Sort the selected elements by their original indices
    topK.sort((a, b) => a.index - b.index);

    
    // // Return only the values of the selected elements
    return topK.map(item => item.value);
};