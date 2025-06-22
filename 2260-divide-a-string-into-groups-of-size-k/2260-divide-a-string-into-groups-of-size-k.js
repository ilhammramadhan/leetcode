/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function(s, k, fill) {
    const n = s.length; 
    const result = [];
    let temp = ""
    for (let i = 0 ; i < n ; i++) {
        temp += s[i];
        if (temp.length === k) {
            result.push(temp);
            temp = ""
        }

       
    }
    if (temp.length > 0 ){
        while (temp.length < k) {
            temp += fill
        }
        result.push(temp);
        temp = ""
    }
    return result;
};