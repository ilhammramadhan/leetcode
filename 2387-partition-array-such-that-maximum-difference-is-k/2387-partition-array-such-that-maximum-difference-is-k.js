/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function(nums, k) {
    let sortNums = nums.sort((a, b) => a - b)
   
    let count = 1;
    let minVal = sortNums[0];
    for (let i = 1 ; i < sortNums.length; i++) {
        if (sortNums[i] - minVal > k ){
            count++;
            minVal = sortNums[i];
        }
    }
    return count; 
};