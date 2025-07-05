/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
     const counts = {};
    for (const num of arr) {
        counts[num] = (counts[num] || 0) + 1;
    }
    let luckyNumber = -1;
    for (const [num, count] of Object.entries(counts)) {
        if (num == count) {
            luckyNumber = Math.max(luckyNumber, num);
        }
    }
    return luckyNumber;
};