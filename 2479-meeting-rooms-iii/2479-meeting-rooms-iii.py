class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # 1. Initialization
        
        # Array to store the count of meetings for each room.
        room_counts = [0] * n
        
        # Min-heap for available rooms, stores room numbers.
        # Initially, all rooms from 0 to n-1 are available.
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Min-heap for busy rooms, stores tuples of (end_time, room_number).
        # This helps us find which room becomes free next.
        busy_rooms = []
        
        # Crucially, sort meetings by their start time.
        meetings.sort()

        # 2. Process Each Meeting
        for start, end in meetings:
            
            # A. Free up rooms that have finished their meetings by the current start time.
            while busy_rooms and busy_rooms[0][0] <= start:
                # Get the room that just became free.
                _ , room_id = heapq.heappop(busy_rooms)
                # Add it back to the available rooms heap.
                heapq.heappush(available_rooms, room_id)
                
            # B. Schedule the current meeting
            
            # Scenario 1: There is an available room.
            if available_rooms:
                # Get the available room with the lowest index.
                room_to_use = heapq.heappop(available_rooms)
                
                # Add this meeting to the busy heap with its end time.
                heapq.heappush(busy_rooms, (end, room_to_use))
                
                # Increment the meeting count for this room.
                room_counts[room_to_use] += 1
            
            # Scenario 2: All rooms are busy, so the meeting is delayed.
            else:
                # Find out which busy room will be free the soonest.
                earliest_free_time, room_to_use = heapq.heappop(busy_rooms)
                
                # The meeting is delayed. The new end time is the room's free time
                # plus the duration of the current meeting.
                duration = end - start
                new_end_time = earliest_free_time + duration
                
                # Put the room back into the busy heap with its new end time.
                heapq.heappush(busy_rooms, (new_end_time, room_to_use))
                
                # Increment the meeting count for this room.
                room_counts[room_to_use] += 1

        # 3. Find the Result
        # Find the room that hosted the most meetings.
        # `max(room_counts)` gives the highest meeting count.
        # `room_counts.index(...)` finds the first index (lowest room number)
        # with that count, handling ties automatically.
        max_meetings = -1
        result_room = -1
        
        for i in range(n):
            if room_counts[i] > max_meetings:
                max_meetings = room_counts[i]
                result_room = i
                
        return result_room