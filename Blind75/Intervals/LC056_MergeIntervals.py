"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""

# Brute Force Solution
# The brute force approach would involve checking every pair of intervals
# to see if they overlap and then merging them. This process is repeated until
# no more intervals can be merged.
#
# This approach is inefficient because it might require repeated passes over
# the list of intervals.


def merge_bruteforce(intervals):
    merged = intervals
    while True:
        merged_once = False
        new_merged = []
        i = 0
        while i < len(merged):
            if i < len(merged) - 1 and merged[i][1] >= merged[i+1][0]:
                new_interval = [merged[i][0], max(
                    merged[i][1], merged[i+1][1])]
                new_merged.append(new_interval)
                merged_once = True
                i += 2  # skip the next interval since it's merged
            else:
                new_merged.append(merged[i])
                i += 1
        if not merged_once:  # if no intervals were merged in this pass
            break
        merged = new_merged
    return merged


# Optimal Solution

# 1.Sort the intervals based on their start times.
# 2.Initialize a result list with the first interval.
# 3.For each subsequent interval:
#   - If it overlaps with the last interval in the result list, merge them.
#   - Otherwise, add it to the result list.

def merge_optimal(intervals):
    if not intervals:
        return []

    # Sort the intervals based on start times
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for i in intervals[1:]:
        # If current interval overlaps with last merged interval
        if i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged.append(i)

    return merged


# Testing both solutions
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]

print([[1, 6], [8, 10], [15, 18]], merge_bruteforce(intervals1))
print([[1, 5]], merge_bruteforce(intervals2))
print()
print([[1, 6], [8, 10], [15, 18]], merge_optimal(intervals1))
print([[1, 5]], merge_optimal(intervals2))
