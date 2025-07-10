import math
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        # 1. Calculate all initial gap lengths and meeting durations.
        # gaps[i] is the free time before meeting i.
        # gaps[n] is the free time after the last meeting.
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(n - 1):
            gaps[i + 1] = startTime[i + 1] - endTime[i]
        gaps[n] = eventTime - endTime[n - 1]

        durations = [0] * n
        for i in range(n):
            durations[i] = endTime[i] - startTime[i]

        # The initial answer is the best we can do without moving anything.
        max_free_time = 0
        for g in gaps:
            max_free_time = max(max_free_time, g)

        # 2. Precompute prefix and suffix maximums of the gaps array.
        # This allows us to quickly find the max of the "other" gaps in O(1).
        prefix_max_gap = [0] * (n + 1)
        prefix_max_gap[0] = gaps[0]
        for i in range(1, n + 1):
            prefix_max_gap[i] = max(prefix_max_gap[i - 1], gaps[i])

        suffix_max_gap = [0] * (n + 2) # Use n+2 for easier indexing
        for i in range(n, -1, -1):
            suffix_max_gap[i] = max(suffix_max_gap[i + 1], gaps[i])

        # 3. Iterate through each meeting as the one to be moved.
        for i in range(n):
            # Get the duration of the meeting we are hypothetically moving.
            moved_duration = durations[i]

            # Calculate the size of the new "super gap" created by moving meeting `i`.
            # This merges gap[i], duration[i], and gap[i+1].
            super_gap_size = gaps[i] + durations[i] + gaps[i+1]

            # Find the largest of the *other* gaps that are not part of the super gap.
            # Using our precomputed arrays makes this fast.
            max_other_gap = 0
            if i > 0:
                # Max of all gaps before gap[i]
                max_other_gap = max(max_other_gap, prefix_max_gap[i - 1])
            if i < n - 1:
                # Max of all gaps after gap[i+1]
                max_other_gap = max(max_other_gap, suffix_max_gap[i + 2])
            
            candidate_free_time = 0
            # Scenario A: The moved meeting fits in one of the other gaps.
            if moved_duration <= max_other_gap:
                candidate_free_time = super_gap_size
            # Scenario B: The moved meeting must be placed back into the super gap.
            else:
                # The result is the max of what's left of the super gap, or the largest of the other gaps.
                candidate_free_time = max(super_gap_size - moved_duration, max_other_gap)
            
            # Update our overall maximum.
            max_free_time = max(max_free_time, candidate_free_time)
            
        return max_free_time