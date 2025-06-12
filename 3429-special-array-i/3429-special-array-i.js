/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function(nums) {
    if (nums.lenght < 2 ){
        return true 
    }
    for (var i = 0 ; i < nums.length ; i++){
        if (nums[i] % 2 === nums [i+1] %2) {
            return false
        }
    }
    return true
};