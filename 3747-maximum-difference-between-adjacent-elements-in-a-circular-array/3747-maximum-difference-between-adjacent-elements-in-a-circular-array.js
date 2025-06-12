/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function(nums) {
     if (nums.length < 2) return 0; // If there are less than 2 elements, no distance can be calculated
    const n = nums.length;
    var maxDistance = 0;

    for (var i = 0; i < nums.length - 1; i++) {
        console.log(nums[i], nums[i + 1])
        const curDistance = (Math.abs(nums[i] - nums[i + 1]))
        maxDistance = Math.max(maxDistance, curDistance);
    }
    const ciruclarDistance = Math.abs(nums[n-1] - nums[0]);
    maxDistance = Math.max(maxDistance, ciruclarDistance);
    return maxDistance;
    
};