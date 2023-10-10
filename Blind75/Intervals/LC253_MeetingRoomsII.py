"""
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:

1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
"""

import heapq


def minMeetingRooms(intervals):
    if len(intervals) == 0:
        return 0
    else:
        # Initialize a heap
        free_rooms = []

        # Sort the intervals based on start times
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting's ending time to the heap
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap
            # If an old room is allocated, then also we have to add to the heap with updated end time
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings
        return len(free_rooms)


intervals = [[0, 30], [5, 10], [15, 20]]
print(2, minMeetingRooms(intervals))
intervals = [[7, 10], [2, 4]]
print(1, minMeetingRooms(intervals))
intervals3 = [[9, 10], [4, 9], [4, 17]]
print(2, minMeetingRooms(intervals))
print()


def minMeetingRooms2(intervals):
    if not intervals:
        return 0

    # Separate out the start and end times
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    start_pointer, end_pointer = 0, 0
    used_rooms = 0

    while start_pointer < len(start_times):
        # If there's a meeting that has ended by the time the meeting at `start_pointer` starts
        if start_times[start_pointer] >= end_times[end_pointer]:
            # Free up a room and increment the end pointer
            used_rooms -= 1
            end_pointer += 1

        # Use a room
        used_rooms += 1

        # Increment the start pointer
        start_pointer += 1

    return max(used_rooms, 0)  # Ensure it doesn't go negative


intervals = [[0, 30], [5, 10], [15, 20]]
print(2, minMeetingRooms2(intervals))
intervals = [[7, 10], [2, 4]]
print(1, minMeetingRooms2(intervals))
intervals3 = [[9, 10], [4, 9], [4, 17]]
print(2, minMeetingRooms2(intervals))
