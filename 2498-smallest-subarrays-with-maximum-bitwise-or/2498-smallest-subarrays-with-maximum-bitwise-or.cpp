class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n);
        // last_pos[k] stores the index of the last number seen (from right to left) 
        // that has the k-th bit set.
        vector<int> last_pos(30, -1);

        // Iterate from the end of the array to the beginning.
        for (int i = n - 1; i >= 0; --i) {
            // 1. Update the last known position for each bit set in nums[i].
            for (int k = 0; k < 30; ++k) {
                // Check if the k-th bit is set in the current number.
                if ((nums[i] >> k) & 1) {
                    last_pos[k] = i;
                }
            }

            // 2. Determine the farthest index we need to reach.
            // This endpoint must be at least the current index i.
            int end_idx = i;
            for (int k = 0; k < 30; ++k) {
                // To get the k-th bit in our OR, we must extend our subarray
                // to at least last_pos[k]. We take the max of all such required endpoints.
                end_idx = max(end_idx, last_pos[k]);
            }
            
            // 3. The length is the distance from i to the farthest required index.
            answer[i] = end_idx - i + 1;
        }
        
        return answer;
    }
};