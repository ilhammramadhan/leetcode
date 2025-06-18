class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Divides an array into n/3 arrays of size 3, where the difference between
        any two elements in one array is less than or equal to k.

        Args:
            nums: The input integer array.
            k: The maximum allowed difference between elements in a subarray.

        Returns:
            A 2D array containing the subarrays, or an empty array if it's
            impossible to satisfy the conditions.
        """
        n = len(nums)
        # 1. Sort the array
        nums.sort()

        result = []

        # 3. Iterate and Form Subarrays
        for i in range(0, n, 3):
            # Ensure we don't go out of bounds if n is not a perfect multiple of 3
            # (though the problem states n is a multiple of 3, it's good practice)
            if i + 2 < n:
                # 3.1. Check Condition
                # Since the array is sorted, the largest element is nums[i+2]
                # and the smallest is nums[i].
                if nums[i+2] - nums[i] <= k:
                    # 3.2. Append to Result
                    result.append([nums[i], nums[i+1], nums[i+2]])
                else:
                    # 3.3. Handle Impossible Case
                    return []
            else:
                # This case should ideally not be hit given n is a multiple of 3
                # but included for robustness. If we don't have 3 elements left,
                # it's an invalid division.
                return []

        # 4. Return Result
        return result