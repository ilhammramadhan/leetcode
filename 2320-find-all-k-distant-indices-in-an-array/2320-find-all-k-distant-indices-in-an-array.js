/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function(nums, key, k) {
     const n = nums.length;
    const result =[]

    const pos = new Set();
    for (let i = 0 ; i<n ; i++){
        if (nums[i] === key){
            pos.add(i)
        }
    }

    for (let i = 0 ; i < n ; i++){
        for (let j of pos){
            if (Math.abs(i - j) <= k){
                result.push(i);
                break; 
            }
        }
    }
    return result;
};