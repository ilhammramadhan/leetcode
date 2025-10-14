class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # The last possible starting index for the first subarray is n - 2*k.
        # We iterate from i = 0 up to and including this index.
        for i in range(n - 2 * k + 1):
            
            # --- Check the first subarray: nums[i:i+k] ---
            first_is_increasing = True
            # We only need to check up to the second-to-last element of the subarray.
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j+1]:
                    first_is_increasing = False
                    break  # Not strictly increasing, so stop checking this subarray
            
            # If the first subarray was increasing, check the second one.
            # If not, we can skip to the next starting position 'i'.
            if first_is_increasing:
                
                # --- Check the second subarray: nums[i+k:i+2*k] ---
                second_is_increasing = True
                start_of_second = i + k
                # We only need to check up to the second-to-last element.
                for j in range(start_of_second, start_of_second + k - 1):
                    if nums[j] >= nums[j+1]:
                        second_is_increasing = False
                        break # Not strictly increasing, stop checking
                
                # If both subarrays passed the test, we've found our answer.
                if second_is_increasing:
                    return True

        # If the loop completes without finding a valid pair, no such pair exists.
        return False