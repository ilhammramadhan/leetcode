/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
     nums.sort((a, b) => a - b); 
    let j = 0, maxLength = 0;
    const n = nums.length;

    for (let i = 0;i<n;i++){
        while(nums[i] - nums[j] > 1) {
            j++;
        }
        if (nums[i] - nums[j] === 1){
            maxLength= Math.max(maxLength, i - j + 1);
        }
    }
    return maxLength
};