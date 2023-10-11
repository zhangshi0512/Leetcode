"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make 
the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are 
non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the 
intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since 
they're already non-overlapping.

Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""

# Brute Force Solution (this might be inefficient for larger inputs)
# 1.Sort the intervals based on their start time.
# 2.Recursively check each interval. At each step, decide whether to include the current interval or skip it.
# 3.If you include an interval, then you skip all the overlapping intervals with it.
# 4.The recursion should return the maximum number of intervals that can be taken.


def eraseOverlapIntervals_bruteforce(intervals):
    # Helper function to determine if two intervals overlap
    def is_overlapping(interval1, interval2):
        return not (interval1[1] <= interval2[0] or interval2[1] <= interval1[0])

    # Recursive function to calculate the maximum number of non-overlapping intervals
    def helper(start_idx):
        if start_idx >= len(intervals):
            return 0

        # Exclude the current interval
        excluded = helper(start_idx + 1)

        # Try including the current interval
        included = 1
        next_idx = start_idx + 1
        while next_idx < len(intervals) and is_overlapping(intervals[start_idx], intervals[next_idx]):
            next_idx += 1
        included += helper(next_idx)

        return max(included, excluded)

    intervals.sort(key=lambda x: x[0])
    max_intervals = helper(0)
    return len(intervals) - max_intervals

# Optimal Solution
# The optimal approach leverages the greedy algorithm:
# 1. Sort the intervals based on their end times.
# 2. Initialize a variable end to negative infinity to track the end of the last processed interval.
# 3. Iterate over the sorted intervals:
#       - If the start of the current interval is greater than or equal to end,
#          then this interval can be added without causing overlap.
#          Update end to the end of this interval.
#       - Otherwise, this interval causes overlap,
#          so increment the count of intervals to be removed.


def eraseOverlapIntervals_optimal(intervals):
    if not intervals:
        return 0

    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])

    end = float('-inf')
    count = 0
    for interval in intervals:
        # If interval doesn't overlap with previous one
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1  # This interval needs to be removed

    return count


# Testing both solutions
intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals2 = [[1, 2], [1, 2], [1, 2]]
intervals3 = [[1, 2], [2, 3]]

print(1, eraseOverlapIntervals_bruteforce(intervals1))
print(2, eraseOverlapIntervals_bruteforce(intervals2))
print(0, eraseOverlapIntervals_bruteforce(intervals3))
print()

# Testing both solutions
intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals2 = [[1, 2], [1, 2], [1, 2]]
intervals3 = [[1, 2], [2, 3]]
print(1, eraseOverlapIntervals_optimal(intervals1))
print(2, eraseOverlapIntervals_optimal(intervals2))
print(0, eraseOverlapIntervals_optimal(intervals3))
