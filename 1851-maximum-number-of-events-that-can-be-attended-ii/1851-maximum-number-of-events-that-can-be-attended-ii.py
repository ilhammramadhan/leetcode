class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Calculates the maximum sum of values from attending at most k events.
        """
        
        # Step 1: Sort events by their start day. This is crucial for the DP approach.
        events.sort()
        
        # Memoization cache to store results of (index, k) pairs.
        # This prevents re-computing the same subproblem.
        memo = {}
        
        # Extract just the start days for efficient binary search later.
        start_days = [event[0] for event in events]
        n = len(events)

        def dp(index: int, count: int) -> int:
            """
            Recursive DP function.
            :param index: The current event index we are considering.
            :param count: The number of events we are still allowed to attend.
            :return: The maximum value we can get from events[index:] with 'count' tickets left.
            """
            
            # Step 6: Base Cases
            # If we have run out of events or out of tickets (k), we can't get any more value.
            if index >= n or count == 0:
                return 0

            # If this state has been computed before, return the cached result.
            if (index, count) in memo:
                return memo[(index, count)]

            # --- The Decision Making Process ---

            # Choice 1: Skip the current event.
            # We move to the next event without using a ticket.
            res_skip = dp(index + 1, count)

            # Choice 2: Attend the current event.
            # We get the value of the current event and find the next non-overlapping event.
            current_event_end_day = events[index][1]
            
            # Step 4: Use binary search to find the first event that starts AFTER the current one ends.
            # bisect_left finds the insertion point for current_event_end_day + 1 in the sorted start_days.
            # This is the index of the next available event.
            next_available_index = bisect.bisect_left(start_days, current_event_end_day + 1)
            
            # The value from this choice is the current event's value plus the max value from the remaining events.
            # We use up one ticket, so the new count is `count - 1`.
            res_attend = events[index][2] + dp(next_available_index, count - 1)
            
            # Step 5: The optimal solution for dp(index, count) is the maximum of the two choices.
            memo[(index, count)] = max(res_skip, res_attend)
            
            return memo[(index, count)]

        # Step 8: Initial call to the DP function, starting with the first event (index 0) and k tickets.
        return dp(0, k)