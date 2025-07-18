class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Calculates the minimum possible difference between the sums of two n-element parts
        after removing n elements from a 3n-element array.
        """
        N = len(nums)
        n = N // 3

        # Step 1: Calculate minimum sums for all prefixes of size >= n
        # prefix_mins[i] will store the sum of the n smallest elements in nums[0...i]
        prefix_mins = [0] * N
        # We use a max-heap to efficiently find the n smallest elements.
        # Python's heapq is a min-heap, so we store negative values to simulate a max-heap.
        max_h = []
        current_sum = 0
        for i in range(N):
            current_sum += nums[i]
            heapq.heappush(max_h, -nums[i])
            
            # If heap has more than n elements, remove the largest one
            if len(max_h) > n:
                # heappop returns the smallest element, which is the largest number's negative.
                # Adding it to the sum is equivalent to subtracting the original number.
                current_sum += heapq.heappop(max_h)
            
            if len(max_h) == n:
                prefix_mins[i] = current_sum

        # Step 2: Calculate maximum sums for all suffixes of size >= n
        # suffix_maxs[i] will store the sum of the n largest elements in nums[i...N-1]
        suffix_maxs = [0] * N
        # We use a min-heap to efficiently find the n largest elements.
        min_h = []
        current_sum = 0
        for i in range(N - 1, -1, -1):
            current_sum += nums[i]
            heapq.heappush(min_h, nums[i])
            
            # If heap has more than n elements, remove the smallest one
            if len(min_h) > n:
                current_sum -= heapq.heappop(min_h)
            
            if len(min_h) == n:
                suffix_maxs[i] = current_sum

        # Step 3: Iterate through possible split points and find the minimum difference
        min_diff = float('inf')
        
        # A split is between index i-1 and i.
        # The prefix must have at least n elements (i-1 >= n-1 => i >= n).
        # The suffix must have at least n elements (N-i >= n => i <= 2n).
        for i in range(n, 2 * n + 1):
            # Min sum from the first part (elements from nums[0...i-1])
            first_part_sum = prefix_mins[i-1]
            
            # Max sum from the second part (elements from nums[i...N-1])
            second_part_sum = suffix_maxs[i]
            
            min_diff = min(min_diff, first_part_sum - second_part_sum)
            
        return min_diff
        