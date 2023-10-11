"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals 
where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval 
and intervals is sorted in ascending order by starti. 

You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted 
in ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

# Brute Force Solution
# 1. Add the newInterval to the intervals.
# 2. Sort the combined list
# 3. Merge the overlapping intervals


def insert_bruteforce(intervals, newInterval):
    # Add the newInterval to the list
    intervals.append(newInterval)

    # Sort the intervals
    intervals.sort(key=lambda x: x[0])

    # Merge overlapping intervals
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Optimal Solution
# 1. Initialize lists for left, right, and merged intervals
# 2. Iterate over the intervals:
#   - If the interval is to the left of newInterval, add it to the left list
#   - If the interval is to the right of newInterval, add it to the right list
#   - Otherwise, it overlaps with newInterval, so merge them
# 3. Return the combined list of left, merged, and right intervals


def insert_optimal(intervals, newInterval):
    left, right = [], []

    for interval in intervals:
        if interval[1] < newInterval[0]:
            left.append(interval)
        elif interval[0] > newInterval[1]:
            right.append(interval)
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    return left + [newInterval] + right


intervals1, newInterval1 = [[1, 3], [6, 9]], [2, 5]
intervals2, newInterval2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]

print([[1, 5], [6, 9]], insert_bruteforce(intervals1, newInterval1))
print([[1, 2], [3, 10], [12, 16]], insert_bruteforce(intervals2, newInterval2))
print()
print([[1, 5], [6, 9]], insert_optimal(intervals1, newInterval1))
print([[1, 2], [3, 10], [12, 16]], insert_optimal(intervals2, newInterval2))
