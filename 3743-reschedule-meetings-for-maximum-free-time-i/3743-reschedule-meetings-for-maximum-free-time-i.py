import collections
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Calculates the maximum continuous free time by finding the largest possible
        gap between 'anchor' meetings.
        """
        n = len(startTime)

        # 1. Calculate all initial gaps and find the maximum among them.
        # This is the baseline answer if we don't form a "mega-gap".
        max_free_time = 0
        if n > 0:
            max_free_time = max(max_free_time, startTime[0]) # First gap
            max_free_time = max(max_free_time, eventTime - endTime[n - 1]) # Last gap
            for i in range(n - 1):
                max_free_time = max(max_free_time, startTime[i + 1] - endTime[i])

        if k == 0:
            return max_free_time

        # 2. Precompute prefix sums of durations to quickly calculate
        # the total duration of a block of meetings.
        durations = [(endTime[i] - startTime[i]) for i in range(n)]
        prefix_durations = [0] * (n + 1)
        for i in range(n):
            prefix_durations[i + 1] = prefix_durations[i] + durations[i]

        # 3. Find the maximum possible "mega-gap".
        # We iterate through each possible starting meeting 'i' of a block of
        # 'k' or fewer "floater" meetings.
        # For each 'i', we want to find the best end meeting 'j' to maximize the free time.
        #
        # The free time for a block i..j is:
        # (space for floaters) - (duration of floaters)
        # = (endTime of anchor j+1 - startTime of anchor i-1) - (durations i..j)
        #
        # To optimize from O(n*k) to O(n), we use a sliding window maximum (deque).
        
        # 'values' holds `startTime[j] - prefix_durations[j]`. We want to find the max
        # of this in a sliding window. Add a value for the eventTime boundary.
        values = [startTime[i] - prefix_durations[i] for i in range(n)]
        values.append(eventTime - prefix_durations[n])

        # deque will store indices into the 'values' array
        dq = collections.deque()

        for i in range(n + 1):
            # Maintain the sliding window of size k+1
            # The window for `i` includes `i` up to `i+k`.
            if dq and dq[0] == i - k - 1:
                dq.popleft()
            
            # Maintain the deque so it's monotonically decreasing.
            while dq and values[dq[-1]] <= values[i]:
                dq.pop()
            dq.append(i)

            # Calculate the mega-gap starting before meeting `i-k` and ending after meeting `dq[0]`.
            # The start of our floater block can be `j = i - k`.
            if i >= k:
                start_floater_idx = i - k
                # Time before the first floater
                prev_end_time = 0 if start_floater_idx == 0 else endTime[start_floater_idx - 1]
                
                # The best end point for this block is given by the max value in the window (dq[0])
                best_end_idx = dq[0]

                space = values[best_end_idx] + prefix_durations[start_floater_idx] - prev_end_time
                max_free_time = max(max_free_time, space)

        return max_free_time