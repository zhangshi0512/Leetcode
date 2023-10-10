"""
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 10^6
"""


def canAttendMeetings(intervals):
    # Sort the intervals based on start times
    intervals.sort(key=lambda x: x[0])

    # Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
            return False
    return True


intervals = [[0, 30], [5, 10], [15, 20]]
print(False, canAttendMeetings(intervals))
intervals = [[7, 10], [2, 4]]
print(True, canAttendMeetings(intervals))
