/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumDeletions = function(word, k) {
     // If the word is empty, no deletions are needed.
    if (!word) {
        return 0;
    }

    // Step 1: Count the frequencies of each character.
    const freqMap = new Map();
    for (const char of word) {
        const count = (freqMap.get(char) || 0) + 1;
        freqMap.set(char, count);
    }

    const originalFreqs = Array.from(freqMap.values());

    // Initialize minDeletions to the worst-case (deleting all characters).
    let minTotalDeletions = word.length;
    
    // Determine a sensible upper bound for our loop
    const maxFreq = Math.max(...originalFreqs);

    // Step 2: Iterate through all possible base frequencies for our target range [baseFreq, baseFreq + k].
    for (let baseFreq = 0; baseFreq <= maxFreq; baseFreq++) {
        const targetMin = baseFreq;
        const targetMax = baseFreq + k;
        let currentTotalDeletions = 0;

        // Step 3: Calculate deletions for the current target range.
        for (const f of originalFreqs) {
            // Case 1: Frequency is below the target range. Delete all occurrences.
            if (f < targetMin) {
                currentTotalDeletions += f;
            } 
            // Case 2: Frequency is above the target range. Delete to reduce it to targetMax.
            else if (f > targetMax) {
                currentTotalDeletions += (f - targetMax);
            }
            // Case 3: Frequency is within the range. No deletions needed.
        }

        // Step 4: Update the overall minimum deletions found so far.
        minTotalDeletions = Math.min(minTotalDeletions, currentTotalDeletions);
    }
    
    // An edge case: if all characters are deleted, the cost is simply the sum of all frequencies
    // This happens implicitly when baseFreq=0 if k=0, but good to consider.
    // If the original word was empty, freqMap is empty, and the loop doesn't run.
    // To handle this, we can return 0 at the start if the word is empty, or if originalFreqs is empty.
    if (originalFreqs.length === 0) {
        return 0;
    }

    return minTotalDeletions;
};