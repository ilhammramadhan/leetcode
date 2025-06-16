/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let maxDiff = -1 
    let curMin = nums [0]
    for ( let i = 0 ; i < nums.length ; i++) {
        if (nums[i] > curMin){
            maxDiff = Math.max(maxDiff , nums[i] - curMin);
        }else {
            curMin = nums[i]
        }
    }
    return maxDiff
};