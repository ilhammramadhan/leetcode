from collections import deque
from bisect import bisect_left, bisect_right
from typing import List

class Router:
    """
    A class to represent a network router that manages data packets with a fixed memory limit.
    """

    def __init__(self, memoryLimit: int):
        """
        Initializes the Router object.

        Args:
            memoryLimit: The maximum number of packets the router can store.
        """
        self.memoryLimit = memoryLimit
        # A deque (double-ended queue) to store packets in FIFO order.
        self.packet_queue = deque()
        # A set to store unique packet tuples for O(1) average time complexity duplicate checks.
        self.packet_set = set()
        # A dictionary to map destination IDs to a sorted list of timestamps.
        # This is for efficient time-range queries in getCount().
        self.destination_timestamps = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """
        Adds a packet to the router.

        Args:
            source: The source identifier of the packet.
            destination: The destination identifier of the packet.
            timestamp: The arrival time of the packet.

        Returns:
            True if the packet is successfully added (i.e., not a duplicate),
            False otherwise.
        """
        packet = (source, destination, timestamp)

        # Check for duplicates using the set.
        if packet in self.packet_set:
            return False

        # If memory limit is reached, remove the oldest packet (FIFO).
        if len(self.packet_queue) == self.memoryLimit:
            oldest_packet_source, oldest_packet_dest, oldest_packet_ts = self.packet_queue.popleft()
            self.packet_set.remove((oldest_packet_source, oldest_packet_dest, oldest_packet_ts))
            
            # Remove the oldest packet's timestamp from the sorted list for its destination.
            self.destination_timestamps[oldest_packet_dest].pop(0)
            # Clean up the list if it becomes empty.
            if not self.destination_timestamps[oldest_packet_dest]:
                del self.destination_timestamps[oldest_packet_dest]

        # Add the new packet to all relevant data structures.
        self.packet_queue.append(packet)
        self.packet_set.add(packet)
        
        # Add the new packet's timestamp to the sorted list for its destination.
        if destination not in self.destination_timestamps:
            self.destination_timestamps[destination] = []
        self.destination_timestamps[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        """
        Forwards the next packet in FIFO order.

        Returns:
            The forwarded packet as a list [source, destination, timestamp].
            Returns an empty list if there are no packets to forward.
        """
        if not self.packet_queue:
            return []

        # Get and remove the oldest packet from the queue.
        packet_source, packet_dest, packet_ts = self.packet_queue.popleft()
        # Remove the packet from the set to maintain consistency.
        self.packet_set.remove((packet_source, packet_dest, packet_ts))
        
        # Remove the forwarded packet's timestamp from the sorted list for its destination.
        self.destination_timestamps[packet_dest].pop(0)
        # Clean up the list if it becomes empty.
        if not self.destination_timestamps[packet_dest]:
            del self.destination_timestamps[packet_dest]
        
        return [packet_source, packet_dest, packet_ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """
        Returns the number of packets currently stored that match the criteria.

        Args:
            destination: The specified destination for the packets.
            startTime: The start of the timestamp range (inclusive).
            endTime: The end of the timestamp range (inclusive).

        Returns:
            The number of packets matching the criteria.
        """
        # If the destination doesn't exist in our map, there are no packets for it.
        if destination not in self.destination_timestamps:
            return 0
        
        timestamps = self.destination_timestamps[destination]

        # Use binary search to find the count of timestamps within the range.
        start_index = bisect_left(timestamps, startTime)
        end_index = bisect_right(timestamps, endTime)

        return end_index - start_index