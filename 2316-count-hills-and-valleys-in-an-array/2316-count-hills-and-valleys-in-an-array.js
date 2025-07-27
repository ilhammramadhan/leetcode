/**
 * @param {number[]} nums
 * @return {number}
 */
var countHillValley = function(nums) {
    // Step 1: Filter the array to remove consecutive duplicates (plateaus).
    const distinctNums = [];
    for (const num of nums) {
        // Only add the number if it's different from the last one added.
        if (distinctNums.length === 0 || distinctNums[distinctNums.length - 1] !== num) {
            distinctNums.push(num);
        }
    }

    // A hill or valley requires at least 3 distinct points.
    if (distinctNums.length < 3) {
        return 0;
    }

    let count = 0;
    
    // Step 2: Iterate from the second to the second-to-last element.
    for (let i = 1; i < distinctNums.length - 1; i++) {
        const left = distinctNums[i - 1];
        const current = distinctNums[i];
        const right = distinctNums[i + 1];

        // Check for a hill (peak)
        if (current > left && current > right) {
            count++;
        }
        
        // Check for a valley
        if (current < left && current < right) {
            count++;
        }
    }

    return count;
};