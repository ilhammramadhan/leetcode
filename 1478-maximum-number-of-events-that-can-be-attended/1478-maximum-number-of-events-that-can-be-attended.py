class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Calculates the maximum number of events that can be attended using a greedy approach.

        The algorithm works as follows:
        1. Sort the events by their start day. This lets us process events chronologically.
        2. Iterate through each day.
        3. Use a min-heap to keep track of the end days of all events that have started but not yet ended.
        4. On each day, attend the available event that will finish the soonest.
        """
        
        # 1. Sort events primarily by their start day.
        events.sort()
        
        # Min-heap to store the end days of events that are currently available to attend.
        min_heap = []
        
        attended_count = 0
        event_index = 0
        num_events = len(events)
        
        # We can find the max day to avoid an unnecessarily long loop, though iterating
        # while there are events to process is also efficient.
        # Let's find the last possible day an event can end.
        last_day = 0
        for start, end in events:
            if end > last_day:
                last_day = end

        # 2. Iterate through each day from the first possible day to the last.
        for day in range(1, last_day + 2): # Loop up to last_day + 1
            
            # Add the end days of all new events that start today into the min-heap.
            while event_index < num_events and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
                
            # Remove events from the min-heap that have already ended (i.e., their end day is before today).
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # If there are events we can attend today, attend the one that finishes the soonest.
            # This is the greedy choice. By popping from the min-heap, we select the event
            # with the smallest end day.
            if min_heap:
                heapq.heappop(min_heap) # "Attend" the event for the current day.
                attended_count += 1
                
        return attended_count