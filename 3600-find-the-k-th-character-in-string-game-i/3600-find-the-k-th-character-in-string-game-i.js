/**
 * @param {number} k
 * @return {character}
 */
var kthCharacter = function(k) {
     // 1. Find the smallest power of 2 length that is >= k.
    let len = 1;
    while (len < k) {
        len *= 2;
    }

    // 2. Work backwards, counting the number of transformations.
    // A transformation occurs when k is in the second half of the current string segment.
    let transformations = 0;
    while (len > 1) {
        let mid = len / 2;
        
        // If k is in the second half...
        if (k > mid) {
            transformations++; // ...increment the transformation count.
            k -= mid;          // ...and adjust k to its corresponding position in the first half.
        }
        
        // Move to the previous (smaller) string segment.
        len = mid;
    }

    // 3. Calculate the final character.
    // The base character is 'a'. The final character is 'a' shifted by `transformations`.
    // We use modulo 26 to handle the wrap-around from 'z' to 'a'.
    const startCharCode = 'a'.charCodeAt(0);
    const finalCharIndex = transformations % 26;
    const finalCharacter = String.fromCharCode(startCharCode + finalCharIndex);

    return finalCharacter;
};