/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
      // If the string is shorter than 3 characters, it can't have three consecutive
    // identical characters, so we can return it as is.
    if (s.length < 3) {
        return s;
    }

    // Use an array to build the result string. Pushing to an array is often
    // more efficient than string concatenation in a loop.
    const result = [];
    
    // We can start the loop from the beginning and check the last two
    // characters added to our result array.
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        const len = result.length;

        // The condition to add a character is that it's not the same as the
        // last two characters already in the result.
        // We only perform this check if the result array has at least 2 elements.
        if (len < 2 || char !== result[len - 1] || char !== result[len - 2]) {
            result.push(char);
        }
    }

    // Join the characters in the array to form the final string.
    return result.join('');
};