/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
      let hasVowel = false
    let hasConsonant = false
    if (word.length < 3) {
        return false
    }

    const vowels = "aiueo"
    const wordLower = word.toLowerCase()

    for (const char of wordLower) {
    const isLetter = char >= 'a' && char <= 'z';
    const isNumber = char >= '0' && char <= '9';

        if (!isLetter && !isNumber) {
        return false;
        }
        // If it's a letter, check if it's a vowel or consonant.
        if (isLetter) {
        if (vowels.includes(char)) {
            hasVowel = true; // Rule 3 is potentially met.
        } else {
            hasConsonant = true; // Rule 4 is potentially met.
        }
        }
    }

     return hasVowel && hasConsonant;
};