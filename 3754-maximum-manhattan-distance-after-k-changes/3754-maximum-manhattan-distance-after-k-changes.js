/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDistance = function(s, k) {
     const n = s.length;

    // Prefix sum arrays to store the (x, y) coordinates at each step.
    // px[i] will be the x-coordinate after i moves.
    // py[i] will be the y-coordinate after i moves.
    // We create arrays of size n+1 and initialize with 0.
    // The element at index 0 represents the starting point (0,0).
    const px = new Array(n + 1).fill(0);
    const py = new Array(n + 1).fill(0);

    // Calculate the original path's coordinates at each step
    for (let i = 0; i < n; i++) {
        const char = s[i];
        // Copy the previous position first
        px[i + 1] = px[i];
        py[i + 1] = py[i];

        // Update the position based on the current move
        switch (char) {
            case 'N':
                py[i + 1]++;
                break;
            case 'S':
                py[i + 1]--;
                break;
            case 'E':
                px[i + 1]++;
                break;
            case 'W':
                px[i + 1]--;
                break;
        }
    }

    // This is the main loop based on the logic described.
    let maxAchievableDistance = 0;

    // We iterate through each possible time 't' from 1 to n
    for (let t = 1; t <= n; t++) {
        // 1. Get the original Manhattan distance at time t.
        //    This is |x_t - x_0| + |y_t - y_0|, which is |px[t]| + |py[t]|
        //    since the origin (x_0, y_0) is (0,0).
        const originalDistAtT = Math.abs(px[t]) + Math.abs(py[t]);

        // 2. Calculate the maximum potential distance at time t using our formula.
        //    - The distance is bounded by the number of steps, 't'.
        //    - Each of the 'k' changes can increase the distance by at most 2.
        const maxDistAtT = Math.min(t, originalDistAtT + 2 * k);

        // 3. Update our overall maximum distance found so far.
        maxAchievableDistance = Math.max(maxAchievableDistance, maxDistAtT);
    }

    return maxAchievableDistance;
};